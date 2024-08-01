from django.db import models
from django.utils import timezone
import uuid
 
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20,unique=True)
    address = models.TextField()
    website=models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time
    updated_at = models.DateTimeField(default=timezone.now)  # Set default to current time


    def __str__(self):
        return self.name

