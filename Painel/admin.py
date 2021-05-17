from django.contrib import admin

# Register your models here.

from .models import DataInfo, Country

admin.site.register(DataInfo)
admin.site.register(Country)

