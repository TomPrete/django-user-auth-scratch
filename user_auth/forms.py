from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'is_premium']

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
