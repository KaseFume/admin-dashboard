from django.urls import path
from .views import *
app_name = 'data'
urlpatterns = [
  path('', admin_dashboard, name='admin_dashboard'),  # Render the admin dashboard on the home page
  path('home',home,name='home'),
  path('adminpanel/', admin_dashboard, name='adminpanel'),
  path('earrings/', earring_view, name='earrings'),
  path('eprset/', eprset, name='eprset'),
  path('handchain/', handchain, name='handchain'),
  path('necklace/', necklace, name='necklace'),
  path('pendant/', pendant, name='pendant'),
  path('ring/', ring, name='ring'),
  path('form/', form_view, name='form'),  # Add/Update form
  path('settings/', settings, name='settings'),  # Utilities page
  path('single-view/', single_view, name='single_view'),
]

