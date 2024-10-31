from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here

@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'base.html')

def home(request):
    return render(request,'pages/home.html')

def earring_view(request):
    # Fetch all Earring objects
    items = Earring.objects.all()

    # Implement search functionality for both ID and name
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(
            Q(id__icontains=search_query) | Q(name__icontains=search_query)
        )

    # Implement sorting
    sort_by = request.GET.get('sort', '')
    if sort_by in ['id', 'name']:
        items = items.order_by(sort_by)

    # Pagination (optional)
    paginator = Paginator(items, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)

    return render(request, 'pages/earring_view.html', {'items': items})

def eprset(request):
    return render(request, 'pages/eprset_view.html')

def handchain(request):
    return render(request, 'pages/handchain_view.html')

def necklace(request):
    return render(request, 'pages/necklace_view.html')

def pendant(request):
    return render(request, 'pages/pendant_view.html')

def ring(request):
    return render(request, 'pages/ring_view.html')

def form_view(request):
    return render(request, 'pages/form.html')

def settings(request):
    return render(request, 'pages/setting.html')

def single_view(request):
    return render(request, 'pages/single-view.html')

def logout_view(request):
    logout(request)  # Logout the user
    return redirect('login')  # Redirect to login page