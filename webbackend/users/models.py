# users/models.py
import uuid
from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

class CustomUserManager(EmailUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class User(EmailAbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    objects = CustomUserManager()  # Assigning CustomUserManager as the default manager

    def __str__(self):
        return self.username