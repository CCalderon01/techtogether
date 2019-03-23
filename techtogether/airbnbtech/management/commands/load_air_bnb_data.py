import csv
from csv import DictReader
import urllib.request

from django.core.management import BaseCommand

from airbnbtech.models import FinalLocation, Location, Transportation, Food

crime_url = 'https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/12cb3883-56f5-47de-afa5-3b1cf61b257b/download/tmp8npb60c9.csv'
contents = urllib.request.urlopen(crime_url)
crime_data = csv.reader(contents)
print(type(crime_data))

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the airbnb data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from listings.csv into our airbnb model"

    def handle(self, *args, **options):
        if FinalLocation.objects.exists() or Location.objects.exists() or Transportation.objects.exists() or Food.objects.exists():
            print('Airbnb data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading airbnb data")
        # for row in DictReader(open('./listings.csv')):
        #     location = Location()
        #     location.name = row['name']
        #     location.url = row['listing_url']
        #     location.id = row['id']
        #     location.neighborhood = row['neighbourhood_cleansed']
        #     location.zip_code = row['zipcode']
        #     location.latitude = row['latitude']
        #     location.longitude = row['longitude']
        #     location.room_type = row['room_type']
        #     location.accomodates = row['accommodates']
        #     location.price = row['price']
        #     location.review_rating = row['review_scores_location']
        #     location.save()
        for row in crime_data:
            if (row['OFFENSE_CODE'] < 3000) and (row['DISTRICT'] != None):
                crime = Crime()
                crime.latitude = row['Lat']
                crime.longitude = row['Long']
                crime.offense_code = row['OFFENSE_CODE']
                crime.save()
