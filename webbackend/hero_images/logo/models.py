from django.db import models
from entity.models import Entity
import uuid

# Create your models here.
class Logo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='media/logo') 
    
    
    