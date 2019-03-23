from django.contrib import admin

# Register your models here.

from .models import FinalLocation, Location, Transportation, Food

@admin.register(FinalLocation)
class FinalAdmin(admin.ModelAdmin):
    list_display = ['url', 'latitude', 'longitude', 'zip_code', 'id',
                    'name', 'neighborhood', 'accomodates', 'room_type',
                    'price', 'review_rating', 'crime_rate', 'food_rate',
                    'transport_rate']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['url', 'latitude', 'longitude', 'zip_code', 'id',
                    'name', 'neighborhood', 'accomodates', 'room_type',
                    'price', 'review_rating']

@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ['latitude', 'longitude', 'name']

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['zip_code', 'name']
