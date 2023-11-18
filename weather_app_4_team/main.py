import requests
import ctk
import sqlite3
import json
import modules.screen  as m_screen
api = ("9a9d833d3cf810e2cce218e2f262a9fa")  
url_api = f"http://api.openweathermap.org/data/2.5/find?q=Dnipro&type=like&APPID=9a9d833d3cf810e2cce218e2f262a9fa"
response = requests.get(url_api)

