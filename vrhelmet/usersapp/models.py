from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class SiteUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_manager = models.BooleanField(default=True)