from django.shortcuts import render

from .forms import *

# Create your views here.

def about(request):
    return render (request, 'about.html')

def login(request):
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)

def register(request):
    register_form = RegisterForm()
    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)