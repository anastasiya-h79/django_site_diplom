from django.contrib import admin
from .models import MethodPay, Delivery, UserInfo, ProductInOrder, Status, Order, ProductInBasket


# Register your models here.
# добавляем товар в заказ
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    search_fields = ['customer_name', 'customer_email', 'status__name']
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

admin.site.register(MethodPay)

admin.site.register(Delivery)


class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']

    class Meta:
        model = UserInfo

admin.site.register(UserInfo, UserInfoAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    search_fields = ['product', 'order']

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)