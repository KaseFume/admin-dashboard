from django.urls import path
from .views import *
app_name = 'data'
urlpatterns = [
  path('', admin_dashboard, name='admin_dashboard'),  # Render the admin dashboard on the home page
  path('home',home,name='home'),
  path('adminpanel/', admin_dashboard, name='adminpanel'),
  path('earrings/', earring_view, name='earrings'),
  path('eprset/', eprset_view, name='eprset'),
  path('handchain/', handchain, name='handchain'),
  path('necklace/', necklace, name='necklace'),
  path('pendant/', pendant, name='pendant'),
  path('ring/', ring, name='ring'),
  path('form/', form_view, name='form'),  # Add/Update form
  path('check-product/<str:product_id>/', check_product, name='check_product'),
  path('add-form/<str:product_id>/', add_form, name='add_form'),
  path('update-form/<str:product_id>/', update_form, name='update_form'),
  path('delete_product/<str:product_id>/',delete_product,name='delete_product'),
  path('settings/', settings_dashboard, name='settings'),  # Utilities page
  path('single-view/', single_view, name='single_view'),
  path('logout/',logout_view,name='logout'),
  path('update_product/<str:product_id>/', update_product, name='update_product')
]

