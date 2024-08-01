from django.db import models
from django.utils import timezone
import uuid
from entity.models import Entity

class Solution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255)
    description = models.TextField()
    ctatext = models.CharField(max_length=255)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, default=None)
    solution_image = models.ImageField(upload_to='media/solutions_images/', null=True, blank=True) # New field for solutions

    created_by = models.CharField(max_length=255)
    created_at = models.DateField() # Set default to current time
    updated_at = models.DateField()  #

    def __str__(self):
        return self.name
