from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here

@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'base.html')


def logout_view(request):
    logout(request)  # Logout the user
    return redirect('login')  # Redirect to login page