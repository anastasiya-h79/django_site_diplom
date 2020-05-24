from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class SiteUser(AbstractUser):
    first_name = models.CharField(max_length=48, blank=True, null=True, default=None)
    #email = models.EmailField(unique=True)
    phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    is_manager = models.BooleanField(default=False)

class Carusel(models.Model):
    image1 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image2 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image3 = models.ImageField(upload_to='carusel', null=True, blank=True)