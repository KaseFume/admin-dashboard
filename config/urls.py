from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('data.urls')),
    path('logout/', include('django.contrib.auth.urls')),
    path('product-detail/',include('prod_detail.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
