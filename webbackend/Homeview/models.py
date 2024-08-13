from django.db import models
from django.conf import settings
from entity.models import Entity

class HomeView(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ctatext = models.CharField(max_length=255)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='homeview_images/')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is saved

    def __str__(self):
        return self.title
