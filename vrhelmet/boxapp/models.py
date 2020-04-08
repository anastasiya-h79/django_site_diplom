from django.db import models

# Create your models here.

class Methodpay(models.Model):
    name = models.CharField(max_length=16)


class Delivery(models.Model):
    name = models.CharField(max_length=16, verbose_name='Выберите способ доставки')


class Userinfo(models.Model):           #на странице оформления заказа в корзине
    name = models.CharField(max_length=32, verbose_name='Имя')
    surname = models.CharField(max_length=32, verbose_name='Фамилия')
    tel = models.IntegerField(verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')


class Box(models.Model):
    name = models.CharField(max_length=16, unique=True)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    num = models.PositiveIntegerField()      #количество товаров
    sum = models.PositiveIntegerField()      # общая сумма за товары
    deliveryprice = models.PositiveIntegerField() #стоимость доставки
    totalpurchse = models.PositiveIntegerField()  # итоговая сумма покупки
    methodpay = models.OneToOneField(Methodpay, on_delete=models.CASCADE)
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE)
    userinfo = models.OneToOneField(Userinfo, on_delete=models.CASCADE)
