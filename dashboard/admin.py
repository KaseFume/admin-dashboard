from django.contrib import admin
from .models import (
    Necklace, EPRSet, Earring, Ring, Handchain, Pendant, Image, ConfidentialData
)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'image', 'date_added')
    search_fields = ('product_id',)

@admin.register(ConfidentialData)
class ConfidentialDataAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'a_ywrt', 'latkha', 'price')
    search_fields = ('product_id',)
    # Restrict access to ConfidentialData unless the user has permissions
    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('app_name.view_confidentialdata')

# Registering product models
admin.site.register(Necklace)
admin.site.register(EPRSet)
admin.site.register(Earring)
admin.site.register(Ring)
admin.site.register(Handchain)
admin.site.register(Pendant)
