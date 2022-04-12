from django.shortcuts import render, redirect, reverse
from .forms import SignUpUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import CreateView
from .models import User

# --- Function Based View Methods ---
def signup_user(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('all_posts'))
    else:
        form = SignUpUserForm()
        return render(request, 'user_auth/signup.html', {'form': form})

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             valid_user = authenticate(username=username, password=password)
#             if valid_user:
#                 login(request, valid_user)
#                 return redirect(reverse('all_posts'))
#             else:
#                 return redirect(reverse('login_user'))

#     else:
#         form = LoginUserForm()
#         return render(request, 'user_auth/login.html', {'form': form})

# def logout_user(request):
#     logout(request)
#     return redirect(reverse('login_user'))


# --- Class Based View Methods ---
class CustomLogoutView(LogoutView):
    next_page = '/blog/'

class SignUp(CreateView):
    model = User
    form_class = SignUpUserForm
    template_name = 'user_auth/signup.html'
    success_url = '/blog/'


