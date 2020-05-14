from django.contrib import admin
from .models import Category, Helmets, Carusel, Message, ProductImages

# Register your models here
# добавляем картинку в класс товара
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
set_active.short_description = "добавить на сайт"

class HelmetsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [ProductImagesInline]
    list_display = ['name', 'category', 'is_active']
    actions = [set_active]

    class Meta:
        model = Helmets

admin.site.register(Helmets, HelmetsAdmin)


admin.site.register(Carusel)


admin.site.register(Message)


class ProductImagesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'is_active']
    actions = [set_active]

    class Meta:
        model = ProductImages

admin.site.register(ProductImages, ProductImagesAdmin)



