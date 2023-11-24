import requests
import modules.screen  as m_screen
import modules.data_base as m_data
api = ("9a9d833d3cf810e2cce218e2f262a9fa")  
url_api = f"http://api.openweathermap.org/data/2.5/find?q=Dnipro&type=like&APPID=9a9d833d3cf810e2cce218e2f262a9fa"
response = requests.get(url_api)

m_data.connection.commit()
m_data.connection.close()
