from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Make sure to include 'accounts.urls'
    path('logout/', include('django.contrib.auth.urls')),  # Optional if using logout view
]
