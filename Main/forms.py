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
        fields = ["site_title", "name", "greeting", "main_designation", "about", "enable_pricing", "enable_services",
                  "enable_posts", "enable_testimonials", "cv", "image"]
        labels = {"image": "Profile Image", "cv": "Resume"}
        exclude = ["pricing", "testimonials", "posts", "services"]
        widgets = {
            'cv': forms.FileInput(attrs={
                'class': 'custom-file-input'
            }),
            'image': forms.FileInput(attrs={
                'class': 'custom-file-input'
            })
        }
