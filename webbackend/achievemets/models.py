from django.db import models
from django.utils import timezone
from customer.models import Customer
from entity.models import Entity

class Achievement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, default=None)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    achievement_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    achievement_image =models.ImageField(upload_to='media/achievement_images/')
       # New field for achievement

    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time
    updated_at = models.DateTimeField(default=timezone.now)  #

    def __str__(self):
        return self.name
