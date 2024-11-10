from django.db import models
from .storage import ClassSpecificStorage  # Import the custom storage class
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils import timezone
def get_upload_path(instance, filename):
    """Generate upload path dynamically based on the product type."""
    model_name = instance.content_type.model  # Get the model name (e.g., 'necklace')
    return f'{model_name}/{instance.object_id}/{instance.object_id}-{filename}'


class Necklace(models.Model):
    id = models.CharField(max_length=255, default="N-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField(blank=True, null=True)
    gems_2 = models.TextField(blank=True, null=True)
    gems_3 = models.TextField(blank=True, null=True)
    a_ywrt = models.TextField(blank=True, null=True)
    latkha = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    purchased = models.BooleanField(blank=True, null=True)
    purchased_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=True)

class EPRSet(models.Model):
    id = models.CharField(max_length=255, default="EPR-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField(blank=True, null=True)
    gems_2 = models.TextField(blank=True, null=True)
    gems_3 = models.TextField(blank=True, null=True)
    a_ywrt = models.TextField(blank=True, null=True)
    latkha = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    purchased = models.BooleanField(blank=True, null=True)
    purchased_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=True)

class Earring(models.Model):
    id = models.CharField(max_length=255, default="E-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField(blank=True, null=True)
    gems_2 = models.TextField(blank=True, null=True)
    gems_3 = models.TextField(blank=True, null=True)
    a_ywrt = models.TextField(blank=True, null=True)
    latkha = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    purchased = models.BooleanField(blank=True, null=True)
    purchased_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=True)

class Ring(models.Model):
    id = models.CharField(max_length=255, default="R-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField(blank=True, null=True)
    gems_2 = models.TextField(blank=True, null=True)
    gems_3 = models.TextField(blank=True, null=True)
    a_ywrt = models.TextField(blank=True, null=True)
    latkha = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    purchased = models.BooleanField(blank=True, null=True)
    purchased_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=True)

class Handchain(models.Model):
    id = models.CharField(max_length=255, default="H-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField(blank=True, null=True)
    gems_2 = models.TextField(blank=True, null=True)
    gems_3 = models.TextField(blank=True, null=True)
    a_ywrt = models.TextField(blank=True, null=True)
    latkha = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    purchased = models.BooleanField(blank=True, null=True)
    purchased_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=True)

class Pendant(models.Model):
    id = models.CharField(max_length=255, default="P-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField(blank=True, null=True)
    gems_2 = models.TextField(blank=True, null=True)
    gems_3 = models.TextField(blank=True, null=True)
    a_ywrt = models.TextField(blank=True, null=True)
    latkha = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    purchased = models.BooleanField(blank=True, null=True)
    purchased_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        # Set purchased_date when purchased is set to True for the first time
        if self.purchased and not self.purchased_date:
            self.purchased_date = timezone.now()
        elif not self.purchased:
            self.purchased_date = None  # Clear the date if `purchased` is set back to False
        super().save(*args, **kwargs)

def get_default_necklace_content_type_id():
    """Retrieve the ContentType ID for the Necklace model."""
    return ContentType.objects.get(app_label='data', model='necklace').id

class Image(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in': ['necklace', 'eprset', 'earring', 'ring', 'handchain', 'pendant']
        },
        default=get_default_necklace_content_type_id
    )
    object_id = models.CharField(max_length=255)
    product = GenericForeignKey('content_type', 'object_id')

    image = models.FileField(
        upload_to=get_upload_path,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.content_type:
            self.content_type = ContentType.objects.get(app_label='data', model='necklace')

        # Auto-generate a unique image name
        image_count = Image.objects.filter(
            content_type=self.content_type, object_id=self.object_id
        ).count()
        self.image.name = f"{image_count + 1}.jpg"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.product}"


# Signal to delete image file from storage when the Image model instance is deleted
@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    """Delete the file from storage when the Image instance is deleted."""
    if instance.image and instance.image.storage.exists(instance.image.name):
        instance.image.storage.delete(instance.image.name)


# Optional: Handle image replacement to delete the old file before saving a new one
@receiver(pre_save, sender=Image)
def delete_old_image_on_change(sender, instance, **kwargs):
    """Delete old image file if the image field is being replaced."""
    if not instance.pk:
        return  # New instance, no replacement needed

    try:
        old_image = Image.objects.get(pk=instance.pk).image
    except Image.DoesNotExist:
        return  # Old image doesn't exist, no action needed

    # If the new image is different from the old one, delete the old one
    if old_image and old_image != instance.image:
        old_image.storage.delete(old_image.name)

class Currency(models.Model):
    # ContentType and Object ID fields for GenericForeignKey setup
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=255)  # Use CharField to support IDs like 'N-3232'
    product = GenericForeignKey('content_type', 'object_id')

    # Currency type choices
    USD = 'USD'
    THB = 'THB'
    MMK = 'MMK'
    CURRENCY_CHOICES = [
        (USD, 'USD'),
        (THB, 'THB'),
        (MMK, 'MMK'),
    ]
    currencyType = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return f"{self.product} - {self.currencyType}"