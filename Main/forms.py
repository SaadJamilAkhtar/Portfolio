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
        fields = "__all__"
        widgets = {
            'cv': forms.FileInput(attrs={
                'class': 'basic-filepond'
            }),
            'image': forms.FileInput(attrs={
                'class': 'image-preview-filepond'
            })
        }
