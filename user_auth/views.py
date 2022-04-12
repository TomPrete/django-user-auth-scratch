from django.shortcuts import render, redirect, reverse
from .forms import SignUpUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup_user(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('all_posts'))
    else:
        form = SignUpUserForm()
        return render(request, 'user_auth/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            valid_user = authenticate(username=username, password=password)
            if valid_user:
                login(request, valid_user)
                return redirect(reverse('all_posts'))
            else:
                return redirect(reverse('login_user'))

    else:
        form = LoginUserForm()
        return render(request, 'user_auth/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(reverse('login_user'))
