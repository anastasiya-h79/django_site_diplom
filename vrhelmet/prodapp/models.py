from django.db import models
from usersapp.models import SiteUser

# https://virtuality.club/store/shlemy_i_ochki_vr_ar_mr/avtonomnie-vr-ochki/


class Category(models.Model):       #этот механизм включает функцию orm, т.е.данные сохраняются в бд
    #создаем поля. из models выбираем тип, в скобках парамерты поля
    name = models.CharField(max_length=100, unique=True)
    #url = models.URLField(max_length=200, verbose_name='vr_шлемы', null=True)
    class Meta:
        verbose_name ='category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Helmets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    #artikul = models.PositiveIntegerField(unique=True)
    text = models.CharField(max_length=84, default='Новое поколение игровых гарнитур')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='helmets', null=True, blank=True)
    price = models.CharField(max_length=16)
    stock = models.CharField(max_length=16)   #срок поставки
    guarantee = models.CharField(max_length=16, blank=True)
    sale = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'helmets'
        verbose_name_plural = 'helmets'


    def __str__(self):
        return self.name


class Carusel(models.Model):
    image1 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image2 = models.ImageField(upload_to='carusel', null=True, blank=True)
    image3 = models.ImageField(upload_to='carusel', null=True, blank=True)


# class HelmetsType(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     url = models.URLField(verbose_name='vr-шлемы')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     helmet = models.ForeignKey(Helmets, on_delete=models.CASCADE)

# Заявка со страницы contactform
class Message(models.Model):
    name = models.CharField(max_length=64, )
    text = models.CharField(max_length=300)
    tel = models.CharField(max_length=16)
    email = models.EmailField(max_length=100)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)








