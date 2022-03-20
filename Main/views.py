from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse

from User.models import *
from .forms import *


def index(request):
    users = Profile.objects.all()
    if users.count() == 0:
        Settings.objects.create()
        Profile.objects.create()
    user = Profile.objects.first()
    if request.POST:
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        settings = Settings.objects.first()
        if settings.from_email:
            send_mail(subject="Hi, Message From Your Idenify", message=f"{message}\n\nFrom : {name}\nEmail : {email}",
                      from_email=settings.from_email, recipient_list=[settings.to_email], auth_user=settings.from_email,
                      auth_password=settings.password)

    data = {
        'user': user
    }

    return render(request, 'index/index1/index.html', data)


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
        'form_title': "Update Service",
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
        'form_title': "Update Portfolio Item",
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
        'form_title': "Update Portfolio Item",
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


@login_required()
def testimonials(request):
    testimonial = Testimonials.objects.all()
    data = {
        'testimonials': testimonial,
        'page_title': "Testimonials",
        'site_title': "Testimonials"
    }
    return render(request, 'testimonials.html', data)


@login_required()
def addTestimonials(request):
    if request.POST:
        form = TestimonialsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('testimonials'))
    form = TestimonialsForm()
    data = {
        'form': form,
        'page_title': "Add Testimonial Entry",
        'site_title': "Add - Testimonial",
        'form_title': "New Testimonial Entry",
        'link': reverse('testimonials'),
        'link_text': "Back",
        'active': "testimonials"
    }
    return render(request, 'form.html', data)


@login_required()
def editTestimonials(request, id):
    testimonial = Testimonials.objects.filter(id=id)
    if testimonial.count() < 1:
        return redirect(reverse('testimonials'))
    testimonial = testimonial.first()
    if request.POST:
        form = TestimonialsForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect(reverse('testimonials'))
    form = TestimonialsForm(instance=testimonial)
    data = {
        'form': form,
        'page_title': "Edit Testimonial",
        'site_title': "Edit - Testimonial",
        'form_title': "Update Testimonial",
        'link': reverse('testimonials'),
        'link_text': "Back",
        'active': "testimonials"
    }
    return render(request, 'form.html', data)


@login_required()
def deleteTestimonials(request, id):
    testimonial = Testimonials.objects.filter(id=id)
    if testimonial.count() < 1:
        return redirect(reverse('testimonials'))
    testimonial = testimonial.first()
    testimonial.delete()
    return redirect(reverse('testimonials'))


@login_required()
def posts(request):
    posts_ = Posts.objects.all()
    data = {
        'posts': posts_,
        'page_title': "Projects",
        'site_title': "Projects"
    }
    return render(request, 'posts.html', data)


@login_required()
def addPosts(request):
    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('posts'))
    form = PostForm()
    data = {
        'form': form,
        'page_title': "Add New Project",
        'site_title': "Add - Project",
        'form_title': "New Project Entry",
        'link': reverse('posts'),
        'link_text': "Back",
        'active': "posts"
    }
    return render(request, 'form.html', data)


@login_required()
def editPosts(request, id):
    post = Posts.objects.filter(id=id)
    if post.count() < 1:
        return redirect(reverse('posts'))
    post = post.first()
    if request.POST:
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('posts'))
    form = PostForm(instance=post)
    data = {
        'form': form,
        'page_title': "Edit Project",
        'site_title': "Edit - Project",
        'form_title': "Update Project",
        'link': reverse('posts'),
        'link_text': "Back",
        'active': "posts"
    }
    return render(request, 'form.html', data)


@login_required()
def deletePosts(request, id):
    post = Posts.objects.filter(id=id)
    if post.count() < 1:
        return redirect(reverse('posts'))
    post = post.first()
    post.delete()
    return redirect(reverse('posts'))


def projectDetails(request, id):
    post = Posts.objects.filter(id=id)
    if post.count() < 1:
        return redirect(reverse('main'))
    post = post.first()
    data = {
        'post': post
    }
    return render(request, 'index/index1/project.html', data)


def EditSettings(request):
    settings = Settings.objects.all().first()
    if request.POST:
        form = EmailSettingForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))
    form = EmailSettingForm(instance=settings)
    data = {
        'form': form,
        'page_title': "Settings",
        'site_title': "Settings",
        'form_title': "Update Settings",
        'link': reverse('dashboard'),
        'link_text': "Back",
        'active': "settings"
    }
    return render(request, 'form.html', data)


def logout_(request):
    logout(request)
    return redirect(reverse('main'))
