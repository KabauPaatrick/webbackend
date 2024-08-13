# locations/models.py
from django.db import models
import uuid
from mptt.models import MPTTModel, TreeForeignKey

class Location(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class DropOffPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(Location, related_name='drop_off_points', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    charges = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.address}"