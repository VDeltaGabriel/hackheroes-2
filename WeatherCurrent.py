"""Example of usage."""
import asyncio
import logging

from aiohttp import ClientError, ClientSession

import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address



def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    LATITUDE = res.latitude
    LONGITUDE = res.longitude
    arraytoget = [LATITUDE, LONGITUDE]
    return(arraytoget)

def GetWeather():
    ip_address = get_ip_address()
    print("IP Address:", ip_address)

    result = printDetails(ip_address)
    print(result[0])
    print(result[1])

    latitude = result[0]
    longitude = result[1]

    #kordy Katowic zostawione w komentarzu dla testów
    #LATITUDE = 50.25833
    #LONGITUDE = 19.0275

    owm = OWM('5df8093e4dcdd9170a57da1b444e4c6d')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_coords(latitude, longitude)
    w = observation.weather
                                     #wszystkie wartości poniżej są orientacyjne (tylko do format-check)
    print(w.detailed_status)         # 'clouds'
    DetailedStatus = w.detailed_status
    #print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.humidity)                # 87
    print(w.temperature('celsius')['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    Temperature = w.temperature('celsius')['temp']
    print(w.temperature('celsius')['feels_like']) # | - |            
    SensedTemperature = w.temperature('celsius')['feels_like']
    #print(w.rain)                    # {}
    #print(w.heat_index)              # None
    print(w.clouds)                  # 75
    return DetailedStatus, Temperature, SensedTemperature
