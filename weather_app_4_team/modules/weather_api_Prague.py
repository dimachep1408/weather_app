from datetime import datetime
import requests
from PIL import Image
import customtkinter

api = ("5c01f4a0f47bf79a74ee7d8b066e45a0")  
url_api = f"http://api.openweathermap.org/data/2.5/weather?q=Prague&type=like&APPID=5c01f4a0f47bf79a74ee7d8b066e45a0&"
response = requests.get(url_api)

data = response.json()

min_temp = int(data["main"]["temp_min"])
max_temp = int(data["main"]["temp_max"])
temp_present = int(data["main"]["temp"])
weather_main = data["weather"][0]["main"]
weather_description = data["weather"][0]["description"]
sunset_time = data["sys"]["sunset"]
sunrise_time = data["sys"]["sunrise"]

sunset_time = datetime.utcfromtimestamp(sunset_time).strftime('%H:%M')
sunrise_time = datetime.utcfromtimestamp(sunrise_time).strftime('%H:%M')

sun = None

weather_main_translate = {
    "Clear": "Безхмарно",
    "Clouds": "Хмарно",
    "Rain": "Дощ",
    "Snow": "Сніг",
}

weather_description_translate = {
    "clear sky": "Чисте небо",
    "few clouds": "Кілька хмар",
   "scattered clouds": "Розсіяні хмари",
    "broken clouds": "Розірвані хмари",
    "overcast clouds": "Пасмурні хмари",
   "light rain": "Легкий дощ",
    "moderate rain": "Помірний дощ",
    "heavy intensity rain": "Сильний дощ",
    "very heavy rain": "Дуже сильний дощ",
    "snow": "Сніг",
    "rain and snow": "Дощ зі снігом",
   "light snow": "Легкий сніг",
    "moderate snow": "Помірний сніг",
    "heavy snow": "Сильний сніг",
    "sleet": "Мокрий сніг",
    "freezing rain": "Град",
    "heavy shower snow": "Снігопад",
    "shower snow": "Злива з снігом",
    "light shower snow": "Легка злива з снігом",
    "light intensity drizzle": "Легкий мряка",
    "drizzle": "Мряка",
    "heavy intensity drizzle": "Сильна мряка",
    "thunderstorm with light rain": "Гроза з легким дощем",
    "thunderstorm with rain": "Гроза з дощем",
    "thunderstorm with heavy rain": "Гроза з сильним дощем",
    "thunderstorm with light snow": "Гроза з легким снігом",
    "thunderstorm with snow": "Гроза зі снігом",
   "thunderstorm with heavy snow": "Гроза з сильним снігом",
    "thunderstorm with light drizzle": "Гроза з легкою мрякою",
   "thunderstorm with drizzle": "Гроза з мрякою",
   "thunderstorm with heavy drizzle": "Гроза з сильною мрякою",
    "fog": "Туман", 
    "Squall": "Шквал",
    "Tornado": "Торнадо"
}


weather_description = weather_description_translate.get(weather_description)
weather_main = weather_main_translate.get(weather_main)

min_temp_celsius = min_temp - 273
max_temp_celsius = max_temp - 273
temp_present_celsius = temp_present - 273

