from django.urls import path
from . import views
app_name="prod_detail"
urlpatterns = [
    path('earring/<str:product_id>/', views.earring_product, name='earring_detail'),
    path('ring/<str:product_id>/', views.ring_product, name='ring_detail'),
    path('pendant/<str:product_id>/', views.pendant_product, name='pendant_detail'),
    path('handchain/<str:product_id>/', views.handchain_product, name='handchain_detail'),
    path('epr-set/<str:product_id>/', views.eprset_product, name='eprset_detail'),
    path('necklace/<str:product_id>/', views.necklace_product, name='necklace_detail'),
]
