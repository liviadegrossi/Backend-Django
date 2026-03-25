from django.shortcuts import render, redirect
from users.forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    login_form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

            # check whether user is registered
            user = auth.authenticate(
                request,
                username = username,
                password = password
            )

            # whether user exists
            if user is not None:
                auth.login(request, user=user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao realizar login!')
                return redirect('login')

    return render(request, 'users/login.html', {'form': login_form})

def registration(request):
    registration_form = RegistrationForm()

    if request.method == 'POST':
        # retrieve the data sent by POST request
        form = RegistrationForm(request.POST)

        # check if the form is valid
        if form.is_valid():

            # check whether the passwords are the same
            if form['password_1'].value() != form['password_2'].value():
                messages.error(request, 'Senhas não são iguais')
                return redirect(registration)
            
            username = form['username'].value()
            email = form['email'].value()
            password = form['password_1'].value()

            # check whether the user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existente')
                return redirect(registration)
            
            # create a new user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
           
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')


    return render(request, 'users/registration.html', {'form': registration_form})