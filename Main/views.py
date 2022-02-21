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
    all_services = Services.objects.all()
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
        'link_text': "Back",
        'active': "services"
    }
    return render(request, 'form.html', data)


@login_required()
def editService(request, id):
    service = Services.objects.filter(id=id)
    if service.count() < 1:
        return redirect(reverse('services'))
    service = service.first()
    if request.POST:
        form = ServicesFom(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect(reverse('services'))
    form = ServicesFom(instance=service)
    data = {
        'form': form,
        'page_title': "Edit Service",
        'site_title': "Edit - Service",
        'form_title': "Updated Service",
        'link': reverse('services'),
        'link_text': "Back",
        'active': "services"
    }
    return render(request, 'form.html', data)


@login_required()
def deleteService(request, id):
    service = Services.objects.filter(id=id)
    if service.count() < 1:
        return redirect(reverse('services'))
    service = service.first()
    service.delete()
    return redirect(reverse('services'))


@login_required()
def portfolio(request):
    all_portfolios = Portfolio.objects.all()
    data = {
        'portfolios': all_portfolios,
        'page_title': "Portfolio items",
        'site_title': "Portfolio"
    }
    return render(request, 'portfolio.html', data)


@login_required()
def addPortfolio(request):
    if request.POST:
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('portfolio'))
    form = PortfolioForm()
    data = {
        'form': form,
        'page_title': "Add Portfolio Item",
        'site_title': "Add - Portfolio",
        'form_title': "New Portfolio Item",
        'link': reverse('portfolio'),
        'link_text': "Back",
        'active': "portfolio"
    }
    return render(request, 'form.html', data)


@login_required()
def editPortfolio(request, id):
    portfolio_ = Portfolio.objects.filter(id=id)
    if portfolio_.count() < 1:
        return redirect(reverse('portfolio'))
    portfolio_ = portfolio_.first()
    if request.POST:
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio_)
        if form.is_valid():
            form.save()
            return redirect(reverse('portfolio'))
    form = PortfolioForm(instance=portfolio_)
    data = {
        'form': form,
        'page_title': "Edit Portfolio Item",
        'site_title': "Edit - Portfolio",
        'form_title': "Updated Portfolio Item",
        'link': reverse('portfolio'),
        'link_text': "Back",
        'active': "portfolio"
    }
    return render(request, 'form.html', data)


@login_required()
def deletePortfolio(request, id):
    portfolio_ = Portfolio.objects.filter(id=id)
    if portfolio_.count() < 1:
        return redirect(reverse('portfolio'))
    portfolio_ = portfolio_.first()
    portfolio_.delete()
    return redirect(reverse('portfolio'))


@login_required()
def pricings(request):
    all_pricing = Pricing.objects.all()
    data = {
        'pricing': all_pricing,
        'page_title': "Pricing Entry",
        'site_title': "Pricing"
    }
    return render(request, 'pricing.html', data)


@login_required()
def addPricing(request):
    if request.POST:
        form = PricingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pricing'))
    form = PricingForm()
    data = {
        'form': form,
        'page_title': "Add Pricing Entry",
        'site_title': "Add - Pricing",
        'form_title': "New Pricing Entry",
        'link': reverse('pricing'),
        'link_text': "Back",
        'active': "pricing"
    }
    return render(request, 'form.html', data)


@login_required()
def editPricing(request, id):
    pricing_ = Pricing.objects.filter(id=id)
    if pricing_.count() < 1:
        return redirect(reverse('pricing'))
    pricing_ = pricing_.first()
    if request.POST:
        form = PricingForm(request.POST, request.FILES, instance=pricing_)
        if form.is_valid():
            form.save()
            return redirect(reverse('pricing'))
    form = PricingForm(instance=pricing_)
    data = {
        'form': form,
        'page_title': "Edit Portfolio Item",
        'site_title': "Edit - Portfolio",
        'form_title': "Updated Portfolio Item",
        'link': reverse('pricing'),
        'link_text': "Back",
        'active': "pricing"
    }
    return render(request, 'form.html', data)


@login_required()
def deletePricing(request, id):
    pricing_ = Pricing.objects.filter(id=id)
    if pricing_.count() < 1:
        return redirect(reverse('pricing'))
    portfolio_ = pricing_.first()
    portfolio_.delete()
    return redirect(reverse('pricing'))