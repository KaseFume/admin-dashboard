import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from data.models import Earring, Handchain, Necklace, EPRSet, Pendant, Ring

def get_product_images(jewelry_type, product_code):
    # Adjusting the path according to your directory structure
    product_folder = os.path.join(settings.MEDIA_ROOT, jewelry_type,product_code)
    if os.path.exists(product_folder):
        return [f'images/{jewelry_type}/{product_code}/{img}' for img in os.listdir(product_folder) if img.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    return []

def earring_product(request, product_id):
    product = get_object_or_404(Earring, id=product_id)
    images = get_product_images('earring', product.id)
    context = {
        'product_code': product.id,
        'name': product.name,
        'total_weight': product.total_weight,
        'gold_net_weight': product.gold_net_weight,
        'gems_1': product.gems_1,
        'gems_2': product.gems_2,
        'gems_3': product.gems_3,
        'a_ywrt': product.a_ywrt,
        'latkha': product.latkha,
        'price': product.price,
        'purchased': product.purchased,
        'images': images,
    }
    return render(request, 'prod_detail/base.html', context)

def handchain_product(request, product_id):
    product = get_object_or_404(Handchain, id=product_id)
    images = get_product_images('handchain', product.id)
    context = {
        'product_code': product.id,
        'name': product.name,
        'total_weight': product.total_weight,
        'gold_net_weight': product.gold_net_weight,
        'gems_1': product.gems_1,
        'gems_2': product.gems_2,
        'gems_3': product.gems_3,
        'a_ywrt': product.a_ywrt,
        'latkha': product.latkha,
        'price': product.price,
        'purchased': product.purchased,
        'images': images,
    }
    return render(request, 'prod_detail/base.html', context)

def necklace_product(request, product_id):
    product = get_object_or_404(Necklace, id=product_id)
    images = get_product_images('necklace', product.id)
    context = {
        'product_code': product.id,
        'name': product.name,
        'total_weight': product.total_weight,
        'gold_net_weight': product.gold_net_weight,
        'gems_1': product.gems_1,
        'gems_2': product.gems_2,
        'gems_3': product.gems_3,
        'a_ywrt': product.a_ywrt,
        'latkha': product.latkha,
        'price': product.price,
        'purchased': product.purchased,
        'images': images,
    }
    return render(request, 'prod_detail/base.html', context)

def eprset_product(request, product_id):
    product = get_object_or_404(EPRSet, id=product_id)
    images = get_product_images('eprset', product.id)
    context = {
        'product_code': product.id,
        'name': product.name,
        'total_weight': product.total_weight,
        'gold_net_weight': product.gold_net_weight,
        'gems_1': product.gems_1,
        'gems_2': product.gems_2,
        'gems_3': product.gems_3,
        'a_ywrt': product.a_ywrt,
        'latkha': product.latkha,
        'price': product.price,
        'purchased': product.purchased,
        'images': images,
    }
    return render(request, 'prod_detail/base.html', context)

def pendant_product(request, product_id):
    product = get_object_or_404(Pendant, id=product_id)
    images = get_product_images('pendant', product.id)
    context = {
        'product_code': product.id,
        'name': product.name,
        'total_weight': product.total_weight,
        'gold_net_weight': product.gold_net_weight,
        'gems_1': product.gems_1,
        'gems_2': product.gems_2,
        'gems_3': product.gems_3,
        'a_ywrt': product.a_ywrt,
        'latkha': product.latkha,
        'price': product.price,
        'purchased': product.purchased,
        'images': images,
    }
    return render(request, 'prod_detail/base.html', context)

def ring_product(request, product_id):
    product = get_object_or_404(Ring, id=product_id)
    images = get_product_images('ring', product.id)
    context = {
        'product_code': product.id,
        'name': product.name,
        'total_weight': product.total_weight,
        'gold_net_weight': product.gold_net_weight,
        'gems_1': product.gems_1,
        'gems_2': product.gems_2,
        'gems_3': product.gems_3,
        'a_ywrt': product.a_ywrt,
        'latkha': product.latkha,
        'price': product.price,
        'purchased': product.purchased,
        'images': images,
    }
    return render(request, 'prod_detail/base.html', context)
