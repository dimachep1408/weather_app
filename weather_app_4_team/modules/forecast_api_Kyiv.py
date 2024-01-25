from datetime import datetime
import requests
import pytz
api = ("5c01f4a0f47bf79a74ee7d8b066e45a0")  
url_api = f"http://api.openweathermap.org/data/2.5/forecast?q=Kyiv&like&APPID=5c01f4a0f47bf79a74ee7d8b066e45a0&"

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
now_kyiv = datetime.now(pytz.timezone("Europe/Kyiv"))

list_events = []
list_temp = []
list_time = []


count = 0


dt = datetime.now()
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
    
            list_events.append({weather_description})
            list_temp.append(temperature)
            list_time.append({dt.strftime('%H:00')})
                    
            print(f"Температура: {temperature}°C")
                
            print(f"Описание: {weather_description}")


#     for count in range(8):
#         list_time.append(dt.strftime('%H:%M'))
#         print(list_time)
    
#         if dt.strftime('%H') == 19:
#             for count in range(8):
#                 if dt.strftime("%H") == 19:
#                     pass
                
# print(dt.strftime("%H"))

# if dt.strftime("%H") == 0:
#     count = 0               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)
# if dt.strftime("%H") == 1:
#     count = 1               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)
# if dt.strftime("%H") == 2:
#     count = 2               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)
# if dt.strftime("%H") == 3:
#     count = 3               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 4:
#     count = 4              
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 5:
#     count = 5               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)
# if dt.strftime("%H") == 6:
#     count = 6               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)


# if dt.strftime("%H") == 7:
#     count = 7               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 8:
#     count = 8               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 9:
#     count = 9               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 10:
#     count = 10               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)
# if dt.strftime("%H") == 11:
#     count = 11               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 12:
#     count = 12               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 13:
#     count = 13               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 14:
#     count = 14               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 15:
#     count = 15               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 16:
#     count = 16               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 17:
#     count = 17               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)
    
# if dt.strftime("%H") == 18:
#     count = 18               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)


# if dt.strftime("%H") == 19:
#     count = 19               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 20:
#     count = 20               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 21:
#     count = 21               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 22:
#     count = 22               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)

# if dt.strftime("%H") == 23:
#     count = 23               
#     for count in range(8):
#         if count == 24:
#             count = 0
#         list_time.append(count)
#         count += 1
#         print(list_time)
