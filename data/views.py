from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q,IntegerField, F
import os
from django.db.models.functions import Cast
import re
# Create your views here

@login_required(login_url='/accounts/send-otp/')
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

    if sort_by == 'id':
        # Fetch items from the database
        items = list(items)

    # Define a function to extract the numeric part for sorting
        def natural_key(item):
        # Use regex to find numeric part of the ID and convert it to integer
            match = re.search(r'\d+', item.id)
            return int(match.group()) if match else 0

    # Sort items using the custom natural key
        items.sort(key=natural_key)

    elif sort_by == 'name':
        items = items.order_by('name')

    # Add all image paths for each item
    for item in items:
        product_folder = os.path.join(settings.MEDIA_ROOT, 'earring', str(item.id))
        if os.path.exists(product_folder):
            item.images = [f'images/earring/{item.id}/{img}' for img in os.listdir(product_folder) if img.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
        else:
            item.images = []  # Empty list if no images found

    # Pagination
    rows_per_page = request.GET.get('rows', 10)  # Default to 10 if not specified
    paginator = Paginator(items, rows_per_page)  # Show dynamic rows per page
    page_number = request.GET.get('page', 1)  # Default to 1 if not specified
    items = paginator.get_page(page_number)

    return render(request, 'pages/earring_view.html', {'items': items, 'rows_per_page': rows_per_page})

def eprset_view(request):
    # Fetch all EPRSet objects
    items = EPRSet.objects.all()

    # Implement search functionality for both ID and name
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(
            Q(id__icontains=search_query) | Q(name__icontains=search_query)
        )

    # Implement sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'id':
        # Define a function to extract the numeric part for sorting
        def natural_key(item):
            match = re.search(r'\d+', item.id)
            return int(match.group()) if match else 0

        items = list(items)
        items.sort(key=natural_key)

    elif sort_by == 'name':
        items = items.order_by('name')

    # Add all image paths for each item
    for item in items:
        product_folder = os.path.join(settings.MEDIA_ROOT, 'eprset', str(item.id))
        if os.path.exists(product_folder):
            item.images = [f'images/eprset/{item.id}/{img}' for img in os.listdir(product_folder) if img.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
        else:
            item.images = []  # Empty list if no images found

    # Pagination
    rows_per_page = request.GET.get('rows', 10)
    paginator = Paginator(items, rows_per_page)
    page_number = request.GET.get('page', 1)
    items = paginator.get_page(page_number)

    return render(request, 'pages/eprset_view.html', {'items': items, 'rows_per_page': rows_per_page})

def handchain(request):
    # Fetch all EPRSet objects
    items = Handchain.objects.all()

    # Implement search functionality for both ID and name
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(
            Q(id__icontains=search_query) | Q(name__icontains=search_query)
        )

    # Implement sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'id':
        # Define a function to extract the numeric part for sorting
        def natural_key(item):
            match = re.search(r'\d+', item.id)
            return int(match.group()) if match else 0

        items = list(items)
        items.sort(key=natural_key)

    elif sort_by == 'name':
        items = items.order_by('name')

    # Add all image paths for each item
    for item in items:
        product_folder = os.path.join(settings.MEDIA_ROOT, 'handchain', str(item.id))
        if os.path.exists(product_folder):
            item.images = [f'images/handchain/{item.id}/{img}' for img in os.listdir(product_folder) if img.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
        else:
            item.images = []  # Empty list if no images found

    # Pagination
    rows_per_page = request.GET.get('rows', 10)
    paginator = Paginator(items, rows_per_page)
    page_number = request.GET.get('page', 1)
    items = paginator.get_page(page_number)
    return render(request, 'pages/handchain_view.html',{'items': items, 'rows_per_page': rows_per_page})

def necklace(request):
    # Fetch all EPRSet objects
    items = Necklace.objects.all()

    # Implement search functionality for both ID and name
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(
            Q(id__icontains=search_query) | Q(name__icontains=search_query)
        )

    # Implement sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'id':
        # Define a function to extract the numeric part for sorting
        def natural_key(item):
            match = re.search(r'\d+', item.id)
            return int(match.group()) if match else 0

        items = list(items)
        items.sort(key=natural_key)

    elif sort_by == 'name':
        items = items.order_by('name')

    # Add all image paths for each item
    for item in items:
        product_folder = os.path.join(settings.MEDIA_ROOT, 'necklace', str(item.id))
        if os.path.exists(product_folder):
            item.images = [f'images/necklace/{item.id}/{img}' for img in os.listdir(product_folder) if img.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
        else:
            item.images = []  # Empty list if no images found

    # Pagination
    rows_per_page = request.GET.get('rows', 10)
    paginator = Paginator(items, rows_per_page)
    page_number = request.GET.get('page', 1)
    items = paginator.get_page(page_number)
    return render(request, 'pages/necklace_view.html',{'items': items, 'rows_per_page': rows_per_page})

def pendant(request):
    # Fetch all EPRSet objects
    items = Pendant.objects.all()

    # Implement search functionality for both ID and name
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(
            Q(id__icontains=search_query) | Q(name__icontains=search_query)
        )

    # Implement sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'id':
        # Define a function to extract the numeric part for sorting
        def natural_key(item):
            match = re.search(r'\d+', item.id)
            return int(match.group()) if match else 0

        items = list(items)
        items.sort(key=natural_key)

    elif sort_by == 'name':
        items = items.order_by('name')

    # Add all image paths for each item
    for item in items:
        product_folder = os.path.join(settings.MEDIA_ROOT, 'pendant', str(item.id))
        if os.path.exists(product_folder):
            item.images = [f'images/pendant/{item.id}/{img}' for img in os.listdir(product_folder) if img.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
        else:
            item.images = []  # Empty list if no images found

    # Pagination
    rows_per_page = request.GET.get('rows', 10)
    paginator = Paginator(items, rows_per_page)
    page_number = request.GET.get('page', 1)
    items = paginator.get_page(page_number)
    return render(request, 'pages/pendant_view.html',{'items': items, 'rows_per_page': rows_per_page})

def ring(request):
    # Fetch all EPRSet objects
    items = Ring.objects.all()

    # Implement search functionality for both ID and name
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(
            Q(id__icontains=search_query) | Q(name__icontains=search_query)
        )

    # Implement sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'id':
        # Define a function to extract the numeric part for sorting
        def natural_key(item):
            match = re.search(r'\d+', item.id)
            return int(match.group()) if match else 0

        items = list(items)
        items.sort(key=natural_key)

    elif sort_by == 'name':
        items = items.order_by('name')

    # Add all image paths for each item
    for item in items:
        product_folder = os.path.join(settings.MEDIA_ROOT, 'ring', str(item.id))
        if os.path.exists(product_folder):
            item.images = [f'images/ring/{item.id}/{img}' for img in os.listdir(product_folder) if img.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
        else:
            item.images = []  # Empty list if no images found

    # Pagination
    rows_per_page = request.GET.get('rows', 10)
    paginator = Paginator(items, rows_per_page)
    page_number = request.GET.get('page', 1)
    items = paginator.get_page(page_number)
    return render(request, 'pages/ring_view.html',{'items': items, 'rows_per_page': rows_per_page})

def form_view(request):
    return render(request, 'pages/form.html')

def settings_dashboard(request):
    return render(request, 'pages/setting.html')

def single_view(request):
    return render(request, 'pages/single-view.html')

def logout_view(request):
    logout(request)  # Logout the user
    return redirect('../../accounts/send-otp/')  # Redirect to login page