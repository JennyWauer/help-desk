from django.db.models import fields
from django.forms import ModelForm, widgets

from django import forms

from .models import Ticket, User

class RegisterForm(ModelForm):
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.TextInput(attrs={'class': 'form-control'}),
            "password": forms.PasswordInput(attrs={'class': 'form-control'}),
        }

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

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = (
            "name",
            "desc",
            "due_date",
            "related_feature",
            "high_priority",
        )

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "desc": forms.TextInput(attrs={'class': 'form-control'}),
            "due_date": forms.DateInput(attrs={'class': 'form-control'}),
            "related_feature": forms.TextInput(attrs={'class': 'form-control'}),
            "high_priority": forms.CheckboxInput(),
        }