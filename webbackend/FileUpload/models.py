# FileUpload/models.py

from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    asset_id = models.CharField(max_length=100)
    public_id = models.CharField(max_length=100)
    model_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.file.name}"
