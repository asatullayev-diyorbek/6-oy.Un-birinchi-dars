from django.contrib import admin
from . import models


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'count', 'price', 'date_manufactured']


admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.Car, CarAdmin)
