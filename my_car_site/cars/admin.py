from django.contrib import admin
from cars.models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('AÑO DE MODELO', {
            "fields":['year']
        }),
        ('FABRICANTE', {
            "fields": ['brand']
        })
    )
    

admin.site.register(Car, CarAdmin)