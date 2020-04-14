from django.db import models

# https://virtuality.club/store/shlemy_i_ochki_vr_ar_mr/avtonomnie-vr-ochki/


class Category(models.Model):       #этот механизм включает функцию orm, т.е.данные сохраняются в бд
    #создаем поля. из models выбираем тип, в скобках парамерты поля
    name = models.CharField(max_length=100, unique=True)
    #url = models.URLField(max_length=200, verbose_name='vr_шлемы', null=True)

    def __str__(self):
        return self.name

class Helmets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    text = models.CharField(max_length=84, default='Новое поколение игровых гарнитур')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='helmets', null=True, blank=True)
    price = models.CharField(max_length=16)
    stock = models.CharField(max_length=16)   #срок поставки
    guarantee = models.CharField(max_length=16, blank=True)
    sale = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


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






