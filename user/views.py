from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from user.forms import LoginForm, RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            user.set_password(raw_password)
            user.save()
            messages.success(
                request, 'Registration successfully!'
            )
            return redirect('pages:home')
    else:
        form = RegisterForm()
    return render(request, 'auth/login-register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            password = cd['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, 'Logging in is successful!'
                )
                return redirect('pages:home')
            else:
                messages.error('Email or password wrong!')
    else:
        form = LoginForm()
    return render(request, 'auth/login-register.html', {'form': form})

def logout_page(request):
    logout(request)
    messages.info(request, 'Exiting...')
    return redirect('pages:')

