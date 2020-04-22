from django.contrib import admin
from .models import Methodpay, Delivery, Userinfo, Order

# Register your models here.
admin.site.register(Methodpay)
admin.site.register(Delivery)
admin.site.register(Userinfo)
admin.site.register(Order)