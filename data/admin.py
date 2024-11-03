from django.contrib import admin
from .models import Necklace, EPRSet, Earring, Ring, Handchain, Pendant, Image,Currency

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'content_type', 'object_id')


admin.site.register(Necklace)
admin.site.register(EPRSet)
admin.site.register(Earring)
admin.site.register(Ring)
admin.site.register(Handchain)
admin.site.register(Pendant)
admin.site.register(Currency)