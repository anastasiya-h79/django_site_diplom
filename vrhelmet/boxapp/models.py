from django.db import models
from prodapp.models import Helmets

# Create your models here.

class Methodpay(models.Model):
    name = models.CharField(max_length=16)


class Delivery(models.Model):
    name = models.CharField(max_length=16, verbose_name='Выберите способ доставки')


#на странице оформления заказа в корзине
class Userinfo(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя')
    surname = models.CharField(max_length=32, verbose_name='Фамилия')
    tel = models.IntegerField(verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    delivery = models.ForeignKey(Delivery, verbose_name='Способ доставки', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, verbose_name='Комментарий к заказу')


class Order(models.Model):
    #name = models.CharField(max_length=16, unique=True)
    #image = models.ImageField()
    #price = models.PositiveIntegerField()
    product = models.ForeignKey(Helmets, on_delete=models.CASCADE)
    num = models.PositiveIntegerField()      #количество товаров
    sum = models.PositiveIntegerField()      # общая сумма за товары
    deliveryprice = models.PositiveIntegerField() #стоимость доставки
    totalpurchase = models.PositiveIntegerField()  # итоговая сумма покупки
    methodpay = models.ForeignKey(Methodpay, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    userinfo = models.ForeignKey(Userinfo, on_delete=models.CASCADE)



