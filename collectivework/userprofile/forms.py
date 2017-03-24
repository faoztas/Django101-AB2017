from django.forms import ModelForm
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password',]
        labels = {
            'email' : 'Eposta',
            'username' : 'Kullanıcı Adı',
            'password' : 'Parola',
        }

        widgets={
            'email' : forms.TextInput(attrs={'placeholder' : 'E-posta'}),
            'username' : forms.TextInput(attrs={'placeholder' : 'Kullanıcı Adı'}),
            'password' : forms.PasswordInput(attrs={'palceholder' : 'Parola'})
        }

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profilephoto']
        labels = {
            'profilephoto' : "Profil Fotoğrafı"
        }

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username',
                  #'password'
                  ]
        labels = {
            'email': "E-posta",
            'username': "Kullanıcı Adı",
            #'password': "Parola",
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-posta', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'class': 'form-control'}),
        }