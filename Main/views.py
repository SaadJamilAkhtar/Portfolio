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
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))
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
            form.save()
    profile = Profile.objects.first()
    form = ProfileForm(instance=profile, initial={'cv': profile.cv.url if profile.cv else None})
    data = {
        "form": form,
        "page_title": "Profile",
        'site_title': "Dashboard"
    }
    return render(request, 'dashboard.html', data)


@login_required()
def resetProfile(request):
    Profile.objects.all().delete()
    Profile.objects.create()
    return redirect(reverse('dashboard'))


@login_required()
def services(request):
    profile = Profile.objects.first()
    all_services = profile.services.all()
    data = {
        'services': all_services,
        'page_title': "Services",
        'site_title': "Services"
    }
    return render(request, 'services.html', data)


@login_required()
def addService(request):
    if request.POST:
        form = ServicesFom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('services'))
    form = ServicesFom()
    data = {
        'form': form,
        'page_title': "Add Service",
        'site_title': "Add - Service",
        'form_title': "New Service",
        'link': reverse('services'),
        'link_text': "Back"
    }
    return render(request, 'form.html', data)
