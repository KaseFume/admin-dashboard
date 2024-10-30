# signals.py
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Necklace, EPRSet, Earring, Ring, Handchain, Pendant, Image

@receiver(post_delete, sender=Necklace)
@receiver(post_delete, sender=EPRSet)
@receiver(post_delete, sender=Earring)
@receiver(post_delete, sender=Ring)
@receiver(post_delete, sender=Handchain)
@receiver(post_delete, sender=Pendant)
def delete_related_images(sender, instance, **kwargs):
    """Delete associated images when a product is deleted."""
    images = Image.objects.filter(object_id=instance.id)
    for image in images:
        image.delete()  # Calls the Image model's delete method
