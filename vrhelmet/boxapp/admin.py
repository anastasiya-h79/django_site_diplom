from django.contrib import admin
from .models import Methodpay, Delivery, Userinfo, Box

# Register your models here.
admin.site.register(Methodpay)
admin.site.register(Delivery)
admin.site.register(Userinfo)
admin.site.register(Box)