from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import logout

from users.forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def log_out(request):
    logout(request)
    return render(request, 'users/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)




