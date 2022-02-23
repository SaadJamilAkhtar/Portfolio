from django import forms
from User.models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-control form-control-xl',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-xl',
            'placeholder': 'Password'
        }
    ))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["site_title", "name", "greeting", "main_designation", "about", "enable_pricing", "pricing",
                  "enable_services", "services", "enable_posts", "posts", "enable_testimonials", "testimonials",
                  "enable_portfolio", "portfolio", "cv", "image"]
        labels = {"image": "Profile Image", "cv": "Resume"}
        widgets = {
            # 'cv': forms.FileInput(attrs={
            #     'class': 'custom-file-input'
            # }),
            # 'image': forms.FileInput(attrs={
            #     'class': 'custom-file-input'
            # }),

        }


class ServicesFom(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__"


class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = "__all__"


class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = '__all__'
