import asyncio
import logging

from aiohttp import ClientError, ClientSession

from accuweather import (
    AccuWeather,
    ApiError,
    InvalidApiKeyError,
    InvalidCoordinatesError,
    RequestsExceededError,
)
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address

ip_address = get_ip_address()
print("IP Address:", ip_address)

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    LATITUDE = res.latitude
    LONGITUDE = res.longitude
    arraytoget = [LATITUDE, LONGITUDE]
    return(arraytoget)


result = printDetails(ip_address)
print(result[0])
print(result[1])

latitude = result[0]
longitude = result[1]


#cordy i api key (cordy zostają te same chyba że mamy sposób na wczytywanie obecnych)
#ustawione na Katowice EDIT: jest już skrypt do generowania geo
#kordy Katowic zostawione w komentarzu dla testów
#LATITUDE = 50.25833
#LONGITUDE = 19.0275

LATITUDE = latitude
LONGITUDE = longitude
API_KEY = "d8SNarC0KGzK45AAAZ9PAS1lzrLYm21U"

logging.basicConfig(level=logging.DEBUG)


async def main():
    """Run main function."""
    async with ClientSession() as websession:
        try:
            accuweather = AccuWeather(
                API_KEY,
                websession,
                latitude=LATITUDE,
                longitude=LONGITUDE,
                language="pl",
            )
            current_conditions = await accuweather.async_get_current_conditions()
            forecast_daily = await accuweather.async_get_daily_forecast(
                days=5, metric=True
            )
            forecast_hourly = await accuweather.async_get_hourly_forecast(
                hours=12, metric=True
            )
        except (
            ApiError,
            InvalidApiKeyError,
            InvalidCoordinatesError,
            ClientError,
            RequestsExceededError,
        ) as error:
            print(f"Error: {error}")
        else:
            print(f"Location: {accuweather.location_name} ({accuweather.location_key})\n") #klucz lokacji accuweather
            print(f"Requests remaining: {accuweather.requests_remaining}\n") #nwm ale jest konieczne (chyba) to chyba możliwe do wykonania requesty na aplikację
            print(f"Current: {current_conditions}\n") #obecny stan pogody
            print(f"Forecast: {forecast_daily}\n") #prognoza dzienna
            print(f"Forecast hourly: {forecast_hourly}\n") #progrnoza godzinna


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()
