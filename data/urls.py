from django.urls import path
from .views import *
app_name = 'data'
urlpatterns = [
  path('', admin_dashboard, name='admin_dashboard'),  # Render the admin dashboard on the home page
  path('adminpanel/', admin_dashboard, name='adminpanel'),
]

