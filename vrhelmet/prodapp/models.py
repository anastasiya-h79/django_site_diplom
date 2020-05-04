from django.utils import timezone
from django.db import models
from usersapp.models import SiteUser


class Category(models.Model):       #этот механизм включает функцию orm, т.е.данные сохраняются в бд
    #создаем поля. из models выбираем тип, в скобках парамерты поля
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name ='category'
        verbose_name_plural = 'categories'


class Helmets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    #artikul = models.PositiveIntegerField(unique=True)
    text = models.CharField(max_length=84, default='Новое поколение игровых гарнитур')
    description = models.TextField(blank=True)
    #image = models.ImageField(upload_to='helmets/', null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    stock = models.CharField(max_length=16)   #срок поставки
    guarantee = models.CharField(max_length=16, blank=True)
    sale = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    #created = models.DateTimeField(auto_now_add=True, auto_now=False, default=timezone.now)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True, default=timezone.now)

    def __str__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class ProductImages(models.Model):
    product = models.ForeignKey(Helmets, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='helmets/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    #created = models.DateTimeField(auto_now_add=True, auto_now=False, default=timezone.now)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True, default=timezone.now)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class Carusel(models.Model):
    image1 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image2 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image3 = models.ImageField(upload_to='carusel', null=True, blank=True)

    class Meta:
        verbose_name = 'carusel_image'
        verbose_name_plural = 'carusel_images'


# Заявка со страницы contactform
class Message(models.Model):
    name = models.CharField(max_length=128)
    #tel = models.CharField(max_length=16)
    email = models.EmailField(max_length=100)
    text = models.CharField(max_length=300)
    #user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.id, self.email)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'








