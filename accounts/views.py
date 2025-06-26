from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
# Create your views here.

class CustomLoginView(LoginView):
    form_class = UserLoginForm
