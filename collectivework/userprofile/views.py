from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.contrib.auth import  logout as user_logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as user_login
from userprofile.forms import UserProfileForm, UserForm, UserUpdateForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from collectivework.settings import LOGIN_URL

# Create your views here.



@csrf_exempt
def login(request):
    data ={}
    note="Lütfen Kullanıcı Adı ve Parolanızı Giriniz"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user_login(request, user)
            next = request.GET.get('next', None)
            if next:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect("/")
        note= "Giriş Başarısız"
    data['text_note']=note
    return render(request, 'userprofile/login.html',data)


@csrf_exempt
def signup(request):
    userprofile_form = UserProfileForm(prefix="userprofile_form")
    user_form = UserForm(prefix="user_form")

    if request.POST:
        userprofile_form = UserProfileForm(request.POST,request.FILES,prefix="userprofile_form")
        user_form = UserForm(request.POST, prefix="user_form")

        if all([userprofile_form.is_valid(),user_form.is_valid()]):
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()
            profile = userprofile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse("userprofile:login"))

    return render(request, "userprofile/signup.html",
                  {'userprofile_form':userprofile_form,'user_form':user_form})



@login_required(login_url=LOGIN_URL)
def logout(request):
    user_logout(request)
    return HttpResponseRedirect("/")



@login_required(login_url=LOGIN_URL)
def update(request):
    data = {'note':'Bilgilerinizi Güncelleyebilirisiniz.'}
    userform = UserUpdateForm(instance=request.user)
    try:
        userprofileform = UserProfileForm(instance=request.user.userprofile)

    except ObjectDoesNotExist:
        userprofileform=UserProfileForm()

    if request.POST:
        userform = UserUpdateForm(request.POST, instance=request.user)

        try:
            userprofileform=UserProfileForm(request.POST,request.FILES,instance=request.user.userprofile)

        except ObjectDoesNotExist:
            userprofileform = UserProfileForm(request.POST,request.FILES)

        if all([userform.is_valid(),userprofileform.is_valid()]):

            user=userform.save()
            profile=userprofileform.save(commit=False)
            profile.user=user
            profile.save()
            data['note']='Bilgileriniz Başarıyla Güncellendi'
        else:
            data['note']='Bilgileriniz Güncellenirken Hata Oluştu!'
    data['user_form']=userform
    data['userprofile_form']=userprofileform
    return render(request, "userprofile/update.html",data)