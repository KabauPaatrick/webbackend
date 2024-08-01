# models.py
from django.db import models
import uuid
from django.utils import timezone
from cloudinary.models import CloudinaryField
from category.models import Category
from brands.models import Brand
from colors.models import Color 



class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    file = CloudinaryField('image')
    asset_id = models.CharField(max_length=255, blank=True, null=True)
    public_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.file.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sold = models.IntegerField(default=0)
    colors = models.ManyToManyField(Color)
    image = models.ImageField(upload_to='media/products_images/')
    tags = models.JSONField(default=list,null=True)
    total_ratings = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    ratings = models.JSONField(default=list)
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
