from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here

@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'base.html')

def home(request):
    return render(request,'pages/home.html')

def earrings(request):
    return render(request, 'pages/earring_view.html')

def eprset(request):
    return render(request, 'pages/eprset.html')

def handchain(request):
    return render(request, 'pages/handchain.html')

def necklace(request):
    return render(request, 'pages/necklace.html')

def pendant(request):
    return render(request, 'pages/pendant.html')

def ring(request):
    return render(request, 'pages/ring.html')

def form_view(request):
    return render(request, 'pages/form.html')

def settings(request):
    return render(request, 'pages/setting.html')

def single_view(request):
    return render(request, 'pages/single-view.html')

def logout_view(request):
    logout(request)  # Logout the user
    return redirect('login')  # Redirect to login page