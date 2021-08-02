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
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        tickets = Ticket.objects.all()
        context = {
            'user': user,
            'tickets': Ticket.objects.all(),
        }
        print(tickets)
        return render(request, 'home.html', context)
    redirect('/login')

def new_ticket(request):
    ticket_form = TicketForm()
    context = {
        'ticket_form': ticket_form
    }
    return render(request, 'new-ticket.html', context)

def profile(request, user_id):
    context = {
        'tickets': Ticket.objects.all()
    }
    return render(request, 'profile.html', context)
    
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
            request.session['user_id'] = new_user.id
            return redirect('/home')
    return redirect('/register')

def user_login(request):
    if request.method == 'GET':
        return redirect('/login')
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/home')
        else:
            messages.error(request, 'Email/password combination not recognized. Please try again!')
        return redirect("/login")

def create_ticket(request):
    if request.method == 'POST':
        errors = Ticket.objects.ticket_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                print(errors)
            return redirect('/new_ticket')
        else:
            if "high_priority" in request.POST:
                high_priority = request.POST['high_priority']
            else: high_priority = False
            new_ticket = Ticket.objects.create(
                name=request.POST['name'],
                desc=request.POST['desc'],
                due_date=request.POST['due_date'],
                high_priority=high_priority,
                user=User.objects.get(id=request.session['user_id'])
            )
            print('hello')
            return redirect('/home')
    return redirect('/home')