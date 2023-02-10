# COMP2040 Python Essentials With Data Analysis
# Assignment 5: Fetching the Weather
# Wai Ping KWOK
# Create a program to fetch the latest weather data from
# the closest weather station calculated by haverine formula
# by accessing the Raspberry Pi Weather Station database
# using a RESTful API
# Created on 2023 01 22
# Sample output:
# [{'air_pressure': 993.23,
#   'air_quality': 67.01,
#   'ambient_temp': -14.02,
#   'created_by': 'MCC Weather Station',
#   'created_on': '2019-01-09T12:24:32Z',
#   'ground_temp': -8.63,
#   'humidity': 44.22,
#   'id': 15124415,
#   'rainfall': 0,
#   'reading_timestamp': '2019-01-09T12:24:32Z',
#   'updated_by': 'MCC Weather Station',
#   'updated_on': '2019-01-09T18:33:09.919Z',
#   'weather_stn_id': 3528546,
#   'wind_direction': 234.06,
#   'wind_gust_speed': 12.97,
#   'wind_speed': 9.38}]

# import libraries
from requests import get
import json
from pprint import pprint
from assignment_5_haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

# location of RRC
my_lat = 49.900983387406384
my_lon = -97.14143503426182


# fetch webpages with JSON data
all_stations = get(stations).json()['items']


def find_closest() -> int:
    """ find the closest weather station
    args:
        empty
    returns:
        closest_station (int): the id of the closest weather station
        in the database.
    """
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)

        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station


closest_stn = find_closest()


# add the station id
weather = weather + str(closest_stn)

# fetch weather data
my_weather = get(weather).json()['items']
pprint(my_weather)
