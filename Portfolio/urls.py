"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from Main.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='main'),
                  path('login', login_, name='login'),
                  path('dashboard', dashboard, name='dashboard'),
                  path('profile/reset', resetProfile, name='reset-profile'),
                  path('services', services, name='services'),
                  path('services/new', addService, name='add-services'),
                  path('services/update/<int:id>', editService, name='edit-services'),
                  path('services/del/<int:id>', deleteService, name='del-services'),
                  path('portfolio', portfolio, name='portfolio'),
                  path('portfolio/new', addPortfolio, name='add-portfolio'),
                  path('portfolio/edit/<int:id>', editPortfolio, name='edit-portfolio'),
                  path('portfolio/del/<int:id>', deletePortfolio, name='del-portfolio'),
                  path('pricings', pricings, name='pricing'),
                  path('pricings/new', addPricing, name='add-pricings'),
                  path('pricings/edit/<int:id>', editPricing, name='edit-pricings'),
                  path('pricings/del/<int:id>', deletePricing, name='del-pricings'),
                  path('testimonials', testimonials, name='testimonials'),
                  path('testimonials/new', addTestimonials, name='add-testimonials'),
                  path('testimonials/edit/<int:id>', editTestimonials, name='edit-testimonials'),
                  path('testimonials/del/<int:id>', deleteTestimonials, name='del-testimonials'),
                  path('projects', posts, name='posts'),
                  path('projects/new', addPosts, name='add-posts'),
                  path('projects/edit/<int:id>', editPosts, name='edit-posts'),
                  path('projects/del/<int:id>', deletePosts, name='del-posts'),
                  path('projects/details/<int:id>', projectDetails, name='project-details')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
