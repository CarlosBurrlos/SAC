from django.db import models

# Create your models here.

class UploadFile(models.Model):
    # Uploads it to MEDIA_ROOT/uploads/
    files = models.FileField(
        upload_to='uploads/',
        blank=True,
        null=True
    )
