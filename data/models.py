# models.py
from django.db import models
from .storage import ClassSpecificStorage  # Import the custom storage class
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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
    purchased = models.BooleanField()

class EPRSet(models.Model):
    id = models.CharField(max_length=255, default="ERP-", primary_key=True)
    name = models.CharField(max_length=255)
    total_weight = models.TextField()
    gold_net_weight = models.TextField()
    gems_1 = models.TextField(blank=True, null=True)
    gems_2 = models.TextField(blank=True, null=True)
    gems_3 = models.TextField(blank=True, null=True)
    a_ywrt = models.TextField(blank=True, null=True)
    latkha = models.TextField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    purchased = models.BooleanField()

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
    purchased = models.BooleanField()

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
    purchased = models.BooleanField()

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
    purchased = models.BooleanField()

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
    purchased = models.BooleanField()

def get_default_necklace_content_type_id():
    """Retrieve the ContentType ID for the Necklace model."""
    return ContentType.objects.get(app_label='data', model='necklace').id

class Image(models.Model):
    # Restrict content_type to only the six jewelry models
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in': [
                'necklace', 'eprset', 'earring', 'ring', 'handchain', 'pendant'
            ]
        },
        default=get_default_necklace_content_type_id  # Use the ID here
    )
    object_id = models.CharField(max_length=255)
    product = GenericForeignKey('content_type', 'object_id')

    # File field with dynamic path based on content type
    image = models.FileField(
        upload_to='get_upload_path',  # Placeholder for the upload path
        storage=ClassSpecificStorage(location='images/'),
        blank=True
    )

    def get_upload_path(self, filename):
        """Generate upload path dynamically based on the product type."""
        model_name = self.content_type.model  # Get the model name (e.g., 'necklace')
        return f'images/{model_name}/{filename}'

    def save(self, *args, **kwargs):
        # Ensure the content_type is set correctly
        if not self.content_type:
            self.content_type = ContentType.objects.get(app_label='data', model='necklace')

        # Auto-generate a unique image name based on the product type and object ID
        image_count = Image.objects.filter(
            content_type=self.content_type, object_id=self.object_id
        ).count()
        self.image.name = f"{self.object_id}-{image_count + 1}.jpg"
        
        # Update the upload path here
        self.image.upload_to = self.get_upload_path(self.image.name)
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Ensure the image file is deleted from storage when the record is deleted
        if self.image and self.image.storage.exists(self.image.name):
            self.image.storage.delete(self.image.name)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.product}"