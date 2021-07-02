from django.forms import ModelForm

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