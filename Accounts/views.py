from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic, View
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordChangeForm

# Create your views here.

# SignUp
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Login
class LoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
# Logout
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    # اضافه کردن پیام موفقیت امیز بودن
# change Password
class PasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_change_done')



