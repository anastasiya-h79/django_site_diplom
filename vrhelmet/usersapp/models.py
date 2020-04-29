from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class SiteUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_manager = models.BooleanField(default=True)

class Carusel(models.Model):
    image1 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image2 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image3 = models.ImageField(upload_to='carusel', null=True, blank=True)