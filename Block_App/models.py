from django.db import models
from _datetime import datetime
import uuid

# Create your models here.

class image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    header = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/',blank=False)
    uploaded_date = models.DateField(default=datetime.now(),blank=False)

    def __str__(self):
        return self.header