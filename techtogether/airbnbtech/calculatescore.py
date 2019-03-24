import csv
from csv import DictReader

#Distance calculation#
def distance(lat1, lon1, lat2, lon2):
    radius = 3956 # miles
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d

#Find minimum distance#
def check_transportation_distance(location1):
    list_distances=[]
    for station in station_list:
            d = distance(station.latitude, station.longitude, location1.latitude, location1.longitude)
            list_distances.append(d)
    min_distance = min(list_distances)
    if min_distance<0.5:
        return "close"
    elif min_distance<1 and min_distance>=0.5:
        return "medium"
    else:
        return "far"

def calculate_food_rating():
    line = 0
    food_dict = {}

    for row in DictReader(open('./food.csv')):
        zipcode = row['ZIP']
        if zipcode in food_dict:
            food_dict[zipcode] = food_dict[zipcode] + 1
        else:
            food_dict[zipcode] = 1
        line += 1

    for zipcode in food_dict:
        food_dict[zipcode] = food_dict[zipcode]/line

    max_value = 0

    for value in food_dict.values():
        if value > max_value:
            max_value = value

    alpha = 5 / max_value

    for zipcode in food_dict:
        food_dict[zipcode] = food_dict[zipcode]*alpha

    return food_dict
