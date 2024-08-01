from django.db import models
from entity.models import Entity

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, default=None)
    testimonial_image =models.ImageField(upload_to='media/testimonial_images/')
    def __str__(self):
        return self.author


# Create your models here.
