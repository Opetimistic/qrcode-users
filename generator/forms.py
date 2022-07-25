from django import forms
from . import models
from django.contrib.auth.models import User


class UserDisplayForm(forms.ModelForm):
    class Meta:
        model = models.UserForm
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=124, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {'password': forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})}


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Password...'})}
