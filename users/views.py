from django.shortcuts import render
from users.forms import LoginForm, RegistrationForm

def login(request):
    login_form = LoginForm()
    return render(request, 'users/login.html', {'form': login_form})

def registration(request):
    registration_form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': registration_form})