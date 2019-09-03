from django.contrib import admin

from .models import CarBrand, CarModel, CarModelInstance

# Register your models here.
# To change how a model is displayed in the admin interface you define a ModelAdmin class (which describes the layout) and register it with the model.

class CarModelInline(admin.TabularInline):
    model = CarModel


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    inlines = [CarModelInline]

class CarModelInstanceInline(admin.TabularInline):
    model = CarModelInstance


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price')
    inlines = [CarModelInstanceInline]

# def display_quantity(self, obj):
# """Return the quantity of this car's instances"""
#         return obj.__class__.objects.count()
#     display_quantity.short_description = 'Quantity'


@admin.register(CarModelInstance)
class CarModelInstanceAdmin(admin.ModelAdmin):
    fields = ['car']