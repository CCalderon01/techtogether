import csv
from csv import DictReader
import urllib.request
import io

from django.core.management import BaseCommand

from airbnbtech.models import FinalLocation, Location, Transportation, Food, Crime

crime_url = 'https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/12cb3883-56f5-47de-afa5-3b1cf61b257b/download/tmp8npb60c9.csv'
# crime_url = 'https://raw.githubusercontent.com/CCalderon01/techtogether/crimedataadd/mock_data.csv'
contents = urllib.request.urlopen(crime_url)
datareader = csv.reader(io.TextIOWrapper(contents))
listData = list(datareader)

index_offense_code = 1
index_latitude = 14
index_longitude = 15

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the airbnb data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

def CheckDataValid(row_to_check):
    data = []
    for cell_t in row_to_check:
        data.append(cell_t)
    cell = data[index_latitude].replace("\'","")
    cell = cell.replace(" ","")
    if not cell:
        return False
    else:
        return True

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from listings.csv into our airbnb model"

    def handle(self, *args, **options):
        if FinalLocation.objects.exists() or Location.objects.exists() or Transportation.objects.exists() or Food.objects.exists():
            print('Airbnb data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading airbnb data")
        for row in DictReader(open('./listings.csv')):
            try:
                location = Location()
                location.name = row['name']
                location.url = row['listing_url']
                location.id = row['id']
                location.neighborhood = row['neighbourhood_cleansed']
                location.zip_code = row['zipcode']
                location.latitude = row['latitude']
                location.longitude = row['longitude']
                location.room_type = row['room_type']
                location.accomodates = row['accommodates']
                location.price = row['price'].strip("$").replace(",","")
                location.review_rating = row['review_scores_rating']
                location.save()
            except ValueError:
                continue
        print("Loading transportation data")
        for row in DictReader(open('./MBTA_coordinates.csv')):
            try:
                transportation = Transportation()
                transportation.latitude = row['Latitude']
                transportation.longitude = row['Longitude']
                transportation.name = row['Name']
                transportation.save()
            except ValueError:
                continue
        print("Loading food data")
        for row in DictReader(open('./food.csv')):
            try:
                food = Food()
                food.name = row['BusinessName']
                food.zip_code = row['ZIP']
                food.save()
            except ValueError:
                continue
        header = True
        print("Loading crime data")
        for row in listData:
            # Checking if the row is a header --> skip
            if header:
                header = False
                continue
            data = []
            for cell in row:
                data.append(cell)
            if CheckDataValid(row):
                crime = Crime()
                crime.latitude = data[index_latitude].replace("\'","")
                crime.longitude = data[index_longitude].replace("\'","")
                try:
                    crime.offense_code = int(data[index_offense_code].replace("\'",""))
                except ValueError:
                    continue
                if(crime.offense_code < 3000):
                    crime.save()
