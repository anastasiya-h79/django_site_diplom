from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from prodapp.models import Helmets

# Create your models here.

class MethodPay(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='methodpay'
        verbose_name_plural = 'methodpays'


class Delivery(models.Model):
    name = models.CharField(max_length=16, verbose_name='Выберите способ доставки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='delivery'
        verbose_name_plural = 'delivery'


#на странице оформления заказа в корзине
class UserInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя')
    surname = models.CharField(max_length=32, verbose_name='Фамилия')
    tel = models.IntegerField(verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    delivery = models.ForeignKey(Delivery, verbose_name='Способ доставки', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, verbose_name='Комментарий к заказу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='userinfo'
        verbose_name_plural = 'userinfo'


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    #created = models.DateTimeField(auto_now_add=True, auto_now=False, default=timezone.now)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True, default=timezone.now)

    def __str__(self):
        return 'Статус %s' % self.name

    class Meta:
        verbose_name ='status'
        verbose_name_plural = 'statuses'


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2,
                                       default=0)  # total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField( max_length=200, blank=True, null=True, default=None )
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, max_length=24, blank=True, null=True, default=None, on_delete=models.CASCADE)
    #created = models.DateTimeField(auto_now_add=True, auto_now=False, default=timezone.now)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True, default=timezone.now)

    def __str__(self):
        return 'Заказ %s %s' % (self.id, self.status.name)

    class Meta:
        verbose_name ='order'
        verbose_name_plural = 'orders'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    #name = models.CharField(max_length=16, unique=True)
    #image = models.ImageField()
    #price = models.PositiveIntegerField()
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Helmets, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.PositiveIntegerField()      #количество товаров
    #sum = models.PositiveIntegerField()      # общая сумма за товары
    price_per_item = models.PositiveIntegerField(default=0)  #текущая цена
    total_price = models.PositiveIntegerField(default=0)  # price*nmb
    deliveryprice = models.PositiveIntegerField() #стоимость доставки
    #totalpurchase = models.PositiveIntegerField()  # итоговая сумма покупки
    methodpay = models.ForeignKey(MethodPay, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    #userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.product.name, self.deliveryprice)

    class Meta:
        verbose_name ='product'
        verbose_name_plural = 'products'

    #переопределим метод save, чтобы цены в заказах пересчитывались автоматически
    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item  #в поле текущей цены записали текущую цену
        self.total_price = self.nmb * price_per_item + self.deliveryprice

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)



