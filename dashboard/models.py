from django.db import models
from django.utils.timezone import now
from .storage import ClassSpecificStorage  # Custom storage class

# Product models for each jewelry type
class Necklace(models.Model):
    id = models.CharField(max_length=255, default="N-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField()
    gems_2 = models.TextField()
    gems_3 = models.TextField()
    date_added = models.DateTimeField(default=now)  # Track when product was added
    purchased = models.BooleanField()

class EPRSet(models.Model):
    id = models.CharField(max_length=255, default="ERP-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField()
    gems_2 = models.TextField()
    gems_3 = models.TextField()
    date_added = models.DateTimeField(default=now)
    purchased = models.BooleanField()

class Earring(models.Model):
    id = models.CharField(max_length=255, default="E-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField()
    gems_2 = models.TextField()
    gems_3 = models.TextField()
    date_added = models.DateTimeField(default=now)
    purchased = models.BooleanField()

class Ring(models.Model):
    id = models.CharField(max_length=255, default="R-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField()
    gems_2 = models.TextField()
    gems_3 = models.TextField()
    date_added = models.DateTimeField(default=now)
    purchased = models.BooleanField()

class Handchain(models.Model):
    id = models.CharField(max_length=255, default="H-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField()
    gems_2 = models.TextField()
    gems_3 = models.TextField()
    date_added = models.DateTimeField(default=now)
    purchased = models.BooleanField()

class Pendant(models.Model):
    id = models.CharField(max_length=255, default="P-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField()
    gems_2 = models.TextField()
    gems_3 = models.TextField()
    date_added = models.DateTimeField(default=now)
    purchased = models.BooleanField()

# Image model to handle multiple product images
class Image(models.Model):
    product_id = models.CharField(max_length=255)  # Store product ID (generic)
    image = models.ImageField(
        upload_to='', storage=ClassSpecificStorage(location='images/'), blank=True
    )
    date_added = models.DateTimeField(default=now)  # Track when image was uploaded

    def save(self, *args, **kwargs):
        # Automatically rename the file based on product ID and image count
        if not self.pk:  # Only rename on first save (new image)
            image_count = Image.objects.filter(product_id=self.product_id).count() + 1
            self.image.name = f"{self.product_id}-{image_count}.jpg"
        super().save(*args, **kwargs)

# Confidential data model for sensitive information
class ConfidentialData(models.Model):
    product_id = models.CharField(max_length=255)  # Link to product ID
    a_ywrt = models.TextField()
    latkha = models.TextField()
    price = models.BigIntegerField()

    class Meta:
        # Ensure this data can only be accessed after login
        permissions = [("view_confidentialdata", "Can view confidential data")]
