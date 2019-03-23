from django.db import models

# Create your models here.

class FinalLocation(models.Model):
    ROOM_TYPE = [('Entire Home', 'E'), ('Private Room', 'P'), ('Shared Space', 'S')]
    url = models.CharField(max_length = 50)
    latitude = models.IntegerField
    longitude = models.IntegerField
    zip_code = models.IntegerField
    id = models.IntegerField
    name = models.CharField(max_length = 60)
    neighborhood = models.CharField(max_length = 30)
    accomodates = models.IntegerField
    room_type = models.CharField(choices = ROOM_TYPE, max_length = 15)
    price = models.IntegerField
    review_rating = models.IntegerField
    #new fields
    crime_rate = models.IntegerField
    food_rate = models.IntegerField
    transport_rate =models.IntegerField
    overall_match = models.IntegerField

class Location  (models.Model):
    ROOM_TYPE = [('Entire Home', 'E'), ('Private Room', 'P'), ('Shared Space', 'S')]
    url = models.CharField(max_length = 50)
    latitude = models.IntegerField
    longitude = models.IntegerField
    zip_code = models.IntegerField
    id = models.IntegerField
    name = models.CharField(max_length = 60)
    neighborhood = models.CharField(max_length = 30)
    accomodates = models.IntegerField
    room_type = models.CharField(choices = ROOM_TYPE, max_length = 15)
    price = models.IntegerField
    review_rating = models.IntegerField

class Transportation (models.Model):
    latitude = models.IntegerField
    longitude = models.IntegerField
    name = models.CharField(max_length = 20)

class Food (models.Model):
    zip_code =  models.IntegerField
    name = models.IntegerField

class Crime(models.Model):
    latitude = models.IntegerField
    longitude = models.IntegerField
    district = models.CharField(max_length = 10)
    offense_code = models.IntegerField