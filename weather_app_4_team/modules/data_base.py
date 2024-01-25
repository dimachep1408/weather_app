import sqlite3 
connection = sqlite3.connect("Weather_data_base.db") 
create_table = ("CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY, Country TEXT NOT NULL,City TEXT NOT NULL,Name TEXT NOT NULL,LastName TEXT NOT NULL)")
cursor = connection.cursor()



