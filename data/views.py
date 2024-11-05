from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q,IntegerField, F
import os
from accounts.models import CustomUser
from django.db.models.functions import Cast
import re
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime
import json
# Create your views here

@login_required(login_url='/accounts/send-otp/')
def admin_dashboard(request):
    return home(request)

@login_required(login_url='/accounts/send-otp/')
def home(request):
    # Retrieve counts for each jewelry type
    total_necklaces = Necklace.objects.count()
    total_epr_sets = EPRSet.objects.count()
    total_earrings = Earring.objects.count()
    total_rings = Ring.objects.count()
    total_handchains = Handchain.objects.count()
    total_pendants = Pendant.objects.count()

    # Retrieve purchased counts for each jewelry type
    purchased_necklaces = Necklace.objects.filter(purchased=True).count()
    purchased_epr_sets = EPRSet.objects.filter(purchased=True).count()
    purchased_earrings = Earring.objects.filter(purchased=True).count()
    purchased_rings = Ring.objects.filter(purchased=True).count()
    purchased_handchains = Handchain.objects.filter(purchased=True).count()
    purchased_pendants = Pendant.objects.filter(purchased=True).count()

    # Total users (including all types of users)
    total_users = CustomUser.objects.count()  # Count users from your CustomUser model

    # Prepare context data
    context = {
        'total_necklaces': total_necklaces,
        'total_epr_sets': total_epr_sets,
        'total_earrings': total_earrings,
        'total_rings': total_rings,
        'total_handchains': total_handchains,
        'total_pendants': total_pendants,
        'purchased_necklaces': purchased_necklaces,
        'purchased_epr_sets': purchased_epr_sets,
        'purchased_earrings': purchased_earrings,
        'purchased_rings': purchased_rings,
        'purchased_handchains': purchased_handchains,
        'purchased_pendants': purchased_pendants,
        'total_users': total_users,
    }

    return render(request, 'pages/home.html', context)

@login_required(login_url='/accounts/send-otp/')
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

@login_required(login_url='/accounts/send-otp/')
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

@login_required(login_url='/accounts/send-otp/')
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

@login_required(login_url='/accounts/send-otp/')
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

@login_required(login_url='/accounts/send-otp/')
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

@login_required(login_url='/accounts/send-otp/')
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

@login_required(login_url='/accounts/send-otp/')
def form_view(request):

    return render(request, 'pages/form.html')

@login_required(login_url='/accounts/send-otp/')
def settings_dashboard(request):
    return render(request, 'pages/setting.html')

@login_required(login_url='/accounts/send-otp/')
def single_view(request):
    return render(request, 'pages/single-view.html')

@login_required(login_url='/accounts/send-otp/')
def logout_view(request):
    logout(request)  # Logout the user
    return redirect('../../accounts/send-otp/')  # Redirect to login page

@login_required(login_url='/accounts/send-otp')
def check_product(request, product_id):
    prefix = product_id.split('-')[0]

    model_map = {
        'E': Earring,
        'N': Necklace,
        'R': Ring,
        'H': Handchain,
        'P': Pendant,
        'EPR': EPRSet
    }

    model = model_map.get(prefix)
    exists = model.objects.filter(id=product_id).exists() if model else False

    if exists:
        return redirect('data:update_form', product_id=product_id)
    else:
        return redirect('data:add_form', product_id=product_id)

@login_required(login_url='/accounts/send-otp')
def add_form(request, product_id):
    # Map prefixes to models and folder names
    model_mapping = {
        'EPR-': EPRSet,
        'E-': Earring,
        'N-': Necklace,
        'R-': Ring,
        'H-': Handchain,
        'P-': Pendant,
    }
    folder_mapping = {
        'EPR-': 'eprset',
        'E-': 'earring',
        'N-': 'necklace',
        'R-': 'ring',
        'H-': 'handchain',
        'P-': 'pendant',
    }

    prefix = None
    product = None

    for pfx, model in model_mapping.items():
        if product_id.startswith(pfx):
            prefix = pfx
            break
    context = {
        'product_id': product_id,
        'selected_prefix': prefix,
    }
    
    return render(request, 'pages/add-form.html',context)

@login_required(login_url='/accounts/send-otp')
def update_form(request, product_id):
    # Map prefixes to models and folder names
    model_mapping = {
        'EPR-': EPRSet,
        'E-': Earring,
        'N-': Necklace,
        'R-': Ring,
        'H-': Handchain,
        'P-': Pendant,
    }
    folder_mapping = {
        'EPR-': 'eprset',
        'E-': 'earring',
        'N-': 'necklace',
        'R-': 'ring',
        'H-': 'handchain',
        'P-': 'pendant',
    }

    prefix = None
    product = None

    for pfx, model in model_mapping.items():
        if product_id.startswith(pfx):
            prefix = pfx
            product = get_object_or_404(model, id=product_id)
            break

    currency = Currency.objects.filter(content_type=ContentType.objects.get_for_model(product), object_id=product_id).first()

    # Get the folder name for the product type
    product_type = folder_mapping.get(prefix, '')

    # Determine the directory and gather existing images
    image_directory = os.path.join(settings.MEDIA_ROOT, product_type, product_id)
    existing_images = []

    if os.path.isdir(image_directory):
        for filename in os.listdir(image_directory):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                existing_images.append(f"/images/{product_type}/{product_id}/{filename}")

    context = {
        'product': product,
        'currency': currency,
        'selected_prefix': prefix,
        'existing_images': existing_images,
    }

    return render(request, 'pages/update-form.html', context)

@login_required
def update_product(request, product_id):
    # Define the model mapping for product types
    model_mapping = {
        'EPR-': EPRSet,
        'E-': Earring,
        'N-': Necklace,
        'R-': Ring,
        'H-': Handchain,
        'P-': Pendant,
    }

    prefix = None
    product = None

    # Find the correct model based on the product ID prefix
    for pfx, model in model_mapping.items():
        if product_id.startswith(pfx):
            prefix = pfx
            product = get_object_or_404(model, id=product_id)
            break

    if request.method == 'POST':
        # Update the product fields
        product.name = request.POST.get('name')
        product.total_weight = request.POST.get('total_weight')
        product.gold_net_weight = request.POST.get('gold_net_weight')
        product.gems_1 = request.POST.get('gems_1')
        product.gems_2 = request.POST.get('gems_2')
        product.gems_3 = request.POST.get('gems_3')
        product.a_ywrt = request.POST.get('a_ywrt')
        product.latkha = request.POST.get('latkha')
        product.price = request.POST.get('price')
        product.purchased = 'purchased' in request.POST
        
        # Update the last_updated field from the form input
        last_updated_str = request.POST.get('lastUpdated')
        if last_updated_str:
            product.last_updated = datetime.strptime(last_updated_str, '%b %d %Y %I:%M %p')

        # Save the product
        product_type = type(product).__name__.lower()  # Get the class name of the product instance
        
        # Handle currency
        selected_currency = request.POST.get('currency')
        currency, created = Currency.objects.get_or_create(
            content_type=ContentType.objects.get_for_model(product),
            object_id=product_id,
            defaults={'currencyType': selected_currency}
        )
        if not created and currency.currencyType != selected_currency:
            currency.currencyType = selected_currency
            currency.save()

        product_directory = os.path.join(settings.MEDIA_ROOT, product_type, product.id)
        # Ensure the directory exists before attempting to access it
        if not os.path.exists(product_directory):
            os.makedirs(product_directory)

        # Handle image uploads
        if 'images' in request.FILES:
            for img in request.FILES.getlist('images'):
                Image.objects.create(product=product, image=img)

        # Handle images to be removed
        images_to_remove_paths = json.loads(request.POST.get('images_to_remove_paths', '[]'))

        for img_path in images_to_remove_paths:
            try:
                if img_path.startswith('/'):
                    img_path = img_path[8:]
                # Attempt to get the image instance using a relative path
                image = Image.objects.get(image=img_path)
                img_path = img_path.replace('\\', '/')
                print(f"{img_path}")
                # Confirm the image file path
                file_path = img_path
                
                # Check if the file exists before deleting
                if os.path.exists(file_path):
                    os.remove(file_path)  # Delete file from storage
                    print(f"Deleted file from storage: {file_path}")
                else:
                    print(f"File not found at path: {file_path}")
                
                # Delete the database record
                image.delete()
                print(f"Deleted Image record from database for path: {img_path}")
                
            except Image.DoesNotExist:
                print(f"Image not found in DB for path: {img_path}")  # Log for debugging
            except Exception as e:
                print(f"Error deleting image {img_path}: {e}")

        product.save()  # Save updated product details

        return form_view(request)

    # Render the update form with existing product data
    return render(request, 'pages/update_form.html', {'product': product})

@login_required
def delete_product(request, product_id):
    # Define the model mapping for product types
    model_mapping = {
        'EPR-': EPRSet,
        'E-': Earring,
        'N-': Necklace,
        'R-': Ring,
        'H-': Handchain,
        'P-': Pendant,
    }

    # Find the correct model based on the product ID prefix
    product = None
    for pfx, model in model_mapping.items():
        if product_id.startswith(pfx):
            product = get_object_or_404(model, id=product_id)
            break

    # If the product was found
    if product:
        # Delete related currency
        content_type = ContentType.objects.get_for_model(product)
        Currency.objects.filter(content_type=content_type, object_id=product_id).delete()

        # Delete related images
        related_images = Image.objects.filter(object_id=product_id)
        for image in related_images:
            # Delete the image file from storage
            file_path = image.image.path
            if os.path.exists(file_path):
                os.remove(file_path)
            # Delete the image record from the database
            image.delete()

        # Delete the product record
        product.delete()

    return form_view(request)

@login_required
def add_product(request, product_id):
    # Define the model mapping for product types
    model_mapping = {
        'EPR-': EPRSet,
        'E-': Earring,
        'N-': Necklace,
        'R-': Ring,
        'H-': Handchain,
        'P-': Pendant,
    }

    # Determine the correct model based on the product ID prefix
    product = None
    for pfx, model in model_mapping.items():
        if product_id.startswith(pfx):
            product_model = model
            break
    else:
        return redirect('some_error_page')  # Handle the case where the prefix is invalid

    if request.method == 'POST':
        # Create a new instance of the determined product model
        product = product_model()
        product.id=product_id
        # Set the fields from the form data
        product.name = request.POST.get('name')
        product.total_weight = request.POST.get('total_weight')
        product.gold_net_weight = request.POST.get('gold_net_weight')
        product.gems_1 = request.POST.get('gems_1')
        product.gems_2 = request.POST.get('gems_2')
        product.gems_3 = request.POST.get('gems_3')
        product.a_ywrt = request.POST.get('a_ywrt')
        product.latkha = request.POST.get('latkha')
        product.price = request.POST.get('price')
        product.purchased = 'purchased' in request.POST
        
        # Set the last_updated field from the form input
        last_updated_str = request.POST.get('lastUpdated')
        if last_updated_str:
            product.last_updated = datetime.strptime(last_updated_str, '%b %d %Y, %I:%M %p')
        else:
            product.last_updated = timezone.now()  # Set default timestamp if not provided

        # Save the product
        product.save()

        # Handle currency
        selected_currency = request.POST.get('currency')
        Currency.objects.create(
            content_type=ContentType.objects.get_for_model(product),
            object_id=product.id,
            currencyType=selected_currency
        )

        # Create a directory for the product's images
        product_type = type(product).__name__.lower()
        product_directory = os.path.join(settings.MEDIA_ROOT, product_type, str(product.id))
        os.makedirs(product_directory, exist_ok=True)

        # Handle image uploads
        if 'images' in request.FILES:
            for img in request.FILES.getlist('images'):
                Image.objects.create(product=product, image=img)

        return form_view(request) # Redirect to a success page after creation

    # Render the add form
    return render(request, 'pages/add_form.html', {'product_model': product_model})