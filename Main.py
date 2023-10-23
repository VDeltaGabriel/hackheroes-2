import time
import WeatherCurrent

while(True):
    DetailedStatus, Temperature, SensedTemperature = WeatherCurrent.GetWeather() 
    print(DetailedStatus)
    print(Temperature)
    print(SensedTemperature)
    time.sleep(1800)

