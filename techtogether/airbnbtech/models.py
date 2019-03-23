from django.db import models

# Create your models here.

class FinalLocation(models.Model):
    ROOM_TYPE = [('Entire Home', 'E'), ('Private Room', 'P'), ('Shared Space', 'S')]
    url = models.CharField(max_length = 50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    zip_code = models.IntegerField(null=True)
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 60)
    neighborhood = models.CharField(max_length = 30)
    accomodates = models.IntegerField(null=True)
    room_type = models.CharField(choices = ROOM_TYPE, max_length = 15)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    review_rating = models.IntegerField(null=True)
    #new fields
    crime_rate = models.IntegerField(null=True)
    food_rate = models.IntegerField(null=True)
    transport_rate =models.IntegerField(null=True)
    overall_match = models.IntegerField(null=True)

class Location  (models.Model):
    ROOM_TYPE = [('Entire Home', 'E'), ('Private Room', 'P'), ('Shared Space', 'S')]
    url = models.CharField(max_length = 50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    zip_code = models.IntegerField(null=True)
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 60)
    neighborhood = models.CharField(max_length = 30)
    accomodates = models.IntegerField(null=True)
    room_type = models.CharField(choices = ROOM_TYPE, max_length = 15)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    review_rating = models.IntegerField(null=True)

class Transportation (models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    name = models.CharField(max_length = 20)

class Food (models.Model):
    zip_code =  models.IntegerField(null=True)
    name = models.CharField(max_length = 40,default='')

class Crime(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    offense_code = models.IntegerField(null=True)
