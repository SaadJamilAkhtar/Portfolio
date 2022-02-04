from django.shortcuts import render
from User.models import *
from .forms import *


def index(request):
    users = Profile.objects.all()
    if users.count() == 0:
        Profile.objects.create()
    user = Profile.objects.first()

    data = {
        'user': user
    }

    return render(request, 'index.html', data)


def login(request):
    if request.POST:
        print(request.POST)
    data = {
        'form': LoginForm()
    }
    return render(request, 'login.html', data)
