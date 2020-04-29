from django.contrib import admin
from .models import *

#Register your models here.
class SiteUserAdmin(admin.ModelAdmin):
    #list_display = ["name", "tel"]
    #list_filter = ['name', ]
    search_fields = ['username', 'email']

    class Meta:
        model = SiteUser


admin.site.register(SiteUser, SiteUserAdmin)
