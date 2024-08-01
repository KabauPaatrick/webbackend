# models.py
from django.db import models
from django.utils import timezone
import uuid

class Color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Create your models here.
