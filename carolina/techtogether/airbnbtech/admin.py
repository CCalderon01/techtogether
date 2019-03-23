from django.contrib import admin

# Register your models here.

from .models import FinalLocation, Location, Transportation, Food, Crime

@admin.register(FinalLocation)
class FinalAdmin(admin.ModelAdmin):
    list_display = ['url', 'latitude', 'longitude', 'zip_code', 'id',
                    'name', 'neighborhood', 'accomodates', 'room_type',
                    'price', 'review_rating', 'crime_rate', 'food_rate',
                    'transport_rate', 'overall_match']

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

@admin.register(Crime)
class CrimeAdmin(admin.ModelAdmin):
    list_display = ['latitude', 'longitude', 'offense_code']
