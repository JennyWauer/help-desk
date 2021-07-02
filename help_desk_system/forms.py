from django.forms import ModelForm, widgets

from django import forms

from .models import User

class RegisterForm(ModelForm):
    confirm_password = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
        )

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "password"
        )

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }