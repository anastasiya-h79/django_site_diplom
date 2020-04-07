from django.db import models

# https://virtuality.club/store/shlemy_i_ochki_vr_ar_mr/avtonomnie-vr-ochki/


class Category(models.Model):       #этот механизм включает функцию orm, т.е.данные сохраняются в бд
    #создаем поля. из models выбираем тип, в скобках парамерты поля
    name = models.CharField(max_length=32, unique=True)


    def __str__(self):
        return self.name

class Helmets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    price = models.CharField(max_length=16)
    stock = models.CharField(max_length=16)   #срок поставки
    guarantee = models.CharField(max_length=16, blank=True)
    sale = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name







