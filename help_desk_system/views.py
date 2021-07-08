from django.shortcuts import render, redirect

from .forms import *

from django.contrib import messages

import bcrypt

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

def home(request):
    return render(request, 'home.html')

def new_ticket(request):
    ticket_form = TicketForm()
    context = {
        'ticket_form': ticket_form
    }
    return render(request, 'new-ticket.html', context)
    
# POST

def new_user(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if User.objects.filter(email=request.POST['email']):
            messages.error(request, 'Email is already registered. Please login!')
            return redirect('/register')
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()    
            new_user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
            )
            request.session['userid'] = new_user.id
            return redirect('/home')
    return redirect('/register')