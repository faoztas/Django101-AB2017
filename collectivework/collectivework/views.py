from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from collectivework.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def index(request):
    return render(request,'base.html')

def help(request):
    return render(request, 'help.html')


def site_rules(request):
    return render(request, 'site_rules.html')


def about(request):
    return render(request, 'about.html')