# main/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '+7 (XXX) XXX-XX-XX'
    }))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('phone_number',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '+7 (XXX) XXX-XX-XX'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))