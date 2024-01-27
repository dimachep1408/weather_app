from datetime import datetime
import requests
import pytz
api = ("5c01f4a0f47bf79a74ee7d8b066e45a0")  
url_api = f"http://api.openweathermap.org/data/2.5/forecast?q=London&like&APPID=5c01f4a0f47bf79a74ee7d8b066e45a0&"

response = requests.get(url_api)
data = response.json()

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
    "sleet": "Мокрий сніг",
    "heavy shower snow": "Снігопад",
    "shower snow": "Злива з снігом",
    "light shower snow": "Легка злива з снігом",
    "rain and snow": "Дощ зі снігом",
    "light rain and snow": "Легкий дощ з снігом",
    "freezing rain": "Град",
   "light snow": "Легкий сніг",
    "moderate snow": "Помірний сніг",
    "heavy snow": "Сильний сніг",
     "moderate snow": "Помірний сніг",
    "sleet": "Мокрий сніг",
    "light intensity drizzle": "Легка мряка",
    "drizzle": "Мряка",
    "heavy intensity drizzle": "Сильна мряка",
    "fog": "Туман",
    "Squall": "Шквал",
    "Tornado": "Торнадо",
    "light thunderstorm": "Невелика гроза",
    "thunderstorm": "Гроза",
    "heavy thunderstorm": "Сильна гроза",
    "thunderstorm with light rain": "Гроза з легким дощем",
    "thunderstorm with rain": "Гроза з дощем",
    "thunderstorm with heavy rain": "Гроза з сильним дощем",
    "thunderstorm with light snow": "Гроза з легким снігом",
    "thunderstorm with snow": "Гроза зі снігом",
   "thunderstorm with heavy snow": "Гроза з сильним снігом",
   "thunderstorm with light drizzle": "Гроза з легкою мрякою",
   "thunderstorm with drizzle": "Гроза з мрякою",
   "thunderstorm with heavy drizzle": "Гроза з сильною мрякою "

}

now_london = datetime.now(pytz.timezone("Europe/London"))

list_events = []
list_temp = []
list_time = []

if "list" in data:
    forecast_list = data["list"]
    
    for forecast in forecast_list:
        dt_txt = forecast.get("dt_txt")
        dt = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
        
        if dt > datetime.now():
            temperature = int(forecast["main"]["temp"]) - 273
            weather_description = forecast["weather"][0]["description"]

            weather_description = weather_description_translate.get(weather_description)
            weather = f"Очікуєтся {weather_description_translate} приблизно о {dt.strftime('%Y-%m-%d %H:%M:%S')}"

            list_events.append({"weather_description": weather_description})
            list_temp.append(temperature)
            list_time.append({dt.strftime('%H:00')})
            
            # print(f"Прогноз на {dt.strftime('%Y-%m-%d %H:%M:%S')}:")
            # print(f"Температура: {temperature}°C")
            # print(f"Описание: {weather_description}")