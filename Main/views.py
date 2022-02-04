from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

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


def login_(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return redirect(reverse('dashboard'))
        print(request.POST)
    data = {
        'form': LoginForm()
    }
    return render(request, 'login.html', data)


@login_required()
def dashboard(request):
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=Profile.objects.first())
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = ProfileForm(instance=Profile.objects.first())
    data = {
        "form": form,
        "page_title": "Profile",
        'site_title': "Dashboard"
    }
    return render(request, 'dashboard.html', data)
