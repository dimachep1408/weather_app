import customtkinter 
import pytz
import modules.weather_api_Dnipro as w_api_D
import modules.weather_api_Kyiv as w_api_K
import modules.weather_api_London as w_api_L
import modules.weather_api_Prague as w_api_P
import modules.weather_api_Rome as w_api_R
import modules.weather_api_Warsaw as w_api_W

import modules.forecast_api_Dnipro as F_W_D
import modules.forecast_api_Kyiv as F_W_K
import modules.forecast_api_London as F_W_L
import modules.forecast_api_Prague as F_W_P
import modules.forecast_api_Rome as F_W_R
# import modules.forecast_api_Warsaw as F_W_W
from datetime import datetime 
import time
from PyQt5 import QtWidgets
from PIL import Image
import os



screen = customtkinter.CTk(fg_color= "#5DA7B1")
screen.withdraw()
screen.title("big screen")
screen.geometry("1200x800")
screen.iconbitmap(r'C:\weather_app_4_team\modules\images\sun_2412787.png')

custom_font = customtkinter.CTkFont(family ="Roboto Slab", size =28, weight ="bold")


user_reg = customtkinter.CTkToplevel(screen, fg_color="#5DA7B1")
user_reg.title("Реєстрація користувача")
user_reg.geometry("460x645")

reg_label = customtkinter.CTkLabel(
    master = user_reg,
    text = "Реєстрація користувача",
    fg_color = "#5DA7B1",
    font = custom_font,
    width = 380,
    height = 55,
    text_color = "white"
    )
reg_label.place(x = 40, y = 50)

min_screen = customtkinter.CTk(fg_color= "#5DA7B1")
min_screen.title("mini screen")
min_screen.state( 'withdrawn')





frame_dekstop = customtkinter.CTkToplevel(fg_color = "#5DA7B1")
frame_dekstop.title("vidjet")
frame_dekstop.state( 'withdrawn')
frame_dekstop.withdraw()
# frame_dekstop.state("iconic")

def click():
    screen.deiconify()

dekstop_vidjet = customtkinter.CTkButton(frame_dekstop,command = click,text = None, corner_radius = 5, fg_color = "#5DA7B1", bg_color = "#5DA7B1", width = 200, height = 200, border_color = "white", hover_color = "#5DA7B1")
min_screen_temp = customtkinter.CTkLabel(frame_dekstop, text= f"{w_api_D.temp_present_celsius}°", width=79, height= 71, font= (custom_font, 79), text_color= "white")
min_screen_weather_event = customtkinter.CTkLabel(frame_dekstop, text = f"{w_api_D.weather_main}", text_color= "white", font= (custom_font, 33))
min_screen_min = customtkinter.CTkLabel(frame_dekstop, text = f"↓{w_api_D.min_temp_celsius}°",text_color= "white", font= (custom_font, 27))
min_screen_max = customtkinter.CTkLabel(frame_dekstop, text = f"↑{w_api_D.max_temp_celsius}°",text_color= "white", font= (custom_font, 27))


dekstop_vidjet.place(x = 0, y = 0)
min_screen_temp.place(x = 50, y = 50)
min_screen_min.place(x = 50, y = 130)
min_screen_max.place(x = 105, y = 130)
min_screen_weather_event.place(x = 60, y = 20)

label_country = customtkinter.CTkLabel(user_reg, text="Країна:", text_color= "white", font=custom_font)
label_country.place(relx=0.5, rely=0.5, x = -166, y =-200 )
entry_country = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 218, text_color = "white", font = custom_font)
entry_country.place(relx=0.5, rely=0.5, x = -175 , y = -150)

country_value = customtkinter.StringVar()



def save_country():
    global coutry
    value = entry_country.get()
    country_value.set(value)
    print("Країна:", country_value.get())
    coutry = country_value.get()

label_town = customtkinter.CTkLabel(user_reg, text="Місто:", text_color= "white", font=custom_font)
label_town.place(relx=0.5, rely=0.5, x = -166, y =-100 )
entry_town = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 218, text_color = "white", font = custom_font)
entry_town.place(relx=0.5, rely=0.5, x = -175 , y = -50)

town_value = customtkinter.StringVar()
def save_town():
    global town
    value = entry_town.get()
    town_value.set(value)
    print("Місто:", town_value.get())
    town = town_value.get()

label_name = customtkinter.CTkLabel(user_reg, text="Ім'я:", text_color= "white", font=custom_font)
label_name.place(relx=0.5, rely=0.5, x = -166, y =0  )
entry_name = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 295, text_color = "white", font = custom_font)
entry_name.place(relx=0.5, rely=0.5, x = -175 , y = 50)

name_value = customtkinter.StringVar()
def save_name():
    global name
    value = entry_name.get()
    name_value.set(value)
    print("Ім'я:", name_value.get())
name = name_value.get()

label_lastname = customtkinter.CTkLabel(user_reg, text="Прізвище:", text_color= "white", font=custom_font, )
label_lastname.place(relx=0.5, rely=0.5, x = -166, y =100 )
entry_lastname = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 295, text_color = "white", font = custom_font)
entry_lastname.place(relx=0.5, rely=0.5, x = -175 , y = 150)

lastname_value = customtkinter.StringVar()
def save_lastname():
    global lastname
    value = entry_lastname.get()
    lastname_value.set(value)
    print("Прізвище:", lastname_value.get())
    lastname = lastname_value.get()

def close_reg():
    personal_button.configure(screen, text="Особистий кабінет ",font=custom_font, command= personal_area,border_color= "#FFFFFF", height=50, width= 282, fg_color= "#5DA7B1",text_color="white",corner_radius= 20, bg_color="#5DA7B1")

    user_area.destroy()


    
def personal_area():


    global label_country_reg, label_town_reg, label_name_reg, label_lastname_reg, label_country, label_town, label_name, label_lastname, user_area
    # temp.grid()
    # temp.grid_forget()

    user_area = customtkinter.CTkToplevel(screen, fg_color="#5DA7B1")
    user_area.title("Особистий кабінет")
    user_area.geometry("460x645")


    label_country_reg = customtkinter.CTkLabel(user_area, text_color= "white",width= 87,height=31, font= (custom_font, 31) )
    label_town_reg = customtkinter.CTkLabel(user_area, text_color= "white",width= 87,height=31, font= (custom_font, 31) )
    label_name_reg = customtkinter.CTkLabel(user_area, text_color= "white",width= 87,height=31, font= (custom_font, 31) )
    label_lastname_reg = customtkinter.CTkLabel(user_area, text_color= "white",width= 87,height=31, font= (custom_font, 31) )

    label_country = customtkinter.CTkLabel(user_area, text="Країна:", text_color= "white", font=custom_font)
    label_town = customtkinter.CTkLabel(user_area, text="Місто:", text_color= "white", font=custom_font)
    label_name = customtkinter.CTkLabel(user_area, text="Ім'я:", text_color= "white", font=custom_font)
    label_lastname = customtkinter.CTkLabel(user_area, text="Прізвище:", text_color= "white", font=custom_font)


    label_country_reg.configure(text = country_value.get())
    label_country_reg.place(x = 128, y = 175)

    label_town_reg.configure(text = town_value.get())
    label_town_reg.place(x = 128 , y = 275)
    

    label_name_reg.configure(text = name_value.get())
    label_name_reg.place(x = 128 , y = 375)

    label_lastname_reg.configure(text = lastname_value.get())
    label_lastname_reg.place(x = 128 , y = 475)

    label_country.place(relx=0.5, rely=0.5, x = -166, y =-200 )
    label_town.place(relx=0.5, rely=0.5, x = -166, y =-100 )
    label_name.place(relx=0.5, rely=0.5, x = -166, y =0  )
    label_lastname.place(relx=0.5, rely=0.5, x = -166, y =100 )

    personal_button.configure(screen, text="повернутися",font=custom_font, command= close_reg,border_color= "#FFFFFF", height=50, width= 282, fg_color= "#5DA7B1",text_color="white",corner_radius= 20, bg_color="#5DA7B1")
    # save_button.place(relx=0.5, rely=0.5, x=200, y=120)
    



frame1 = customtkinter.CTkFrame(screen, width= 1200, height= 800, border_color= "#096C82",  fg_color= "#5DA7B1", corner_radius= 20, border_width= 5 )
frame2 = customtkinter.CTkFrame(screen, width= 275, height= 800, border_color= "#096C82",  fg_color= "#096C82", corner_radius= 20, border_width= 5 )

ukraine_timezone = "Europe/Kyiv"
london_timezone = "Europe/London"
prague_timezone = "Europe/Prague"
rome_timezone = "Europe/Rome"
warsaw_timezone = "Europe/Warsaw"

now_dnipro = datetime.now(pytz.timezone(ukraine_timezone))
date_dnipro = now_dnipro.strftime("%d/%m/%Y")
time_oclock_dnipro = now_dnipro.strftime("%H:%M")
day = datetime.today().isoweekday()

now_kyiv = datetime.now(pytz.timezone(ukraine_timezone))
date_kyiv = now_kyiv.strftime("%d/%m/%Y")
time_oclock_kyiv = now_kyiv.strftime("%H:%M")
day = datetime.today().isoweekday()

now_london = datetime.now(pytz.timezone(london_timezone))
date_london = now_london.strftime("%d/%m/%Y")
time_oclock_london = now_london.strftime("%H:%M")
day = datetime.today().isoweekday()

now_prague = datetime.now(pytz.timezone(prague_timezone))
date_prague = now_prague.strftime("%d/%m/%Y")
time_oclock_prague = now_prague.strftime("%H:%M")
day = datetime.today().isoweekday()

now_rome = datetime.now(pytz.timezone(rome_timezone))
date_rome = now_rome.strftime("%d/%m/%Y")
time_oclock_rome = now_rome.strftime("%H:%M")
day = datetime.today().isoweekday()

now_warsaw = datetime.now(pytz.timezone(warsaw_timezone))
date_warsaw = now_warsaw.strftime("%d/%m/%Y")
time_oclock_warsaw = now_warsaw.strftime("%H:%M")
day = datetime.today().isoweekday()


if day == 1:
    day = "Понеділок"
elif day == 2 :
    day = "Вівторок"
elif day == 3:
    day = "Середа"
elif day == 4:
    day = "Четверг"
if day == 5:
    day = "П'ятниця"
elif day == 6:
    day = "Субота"
elif day == 6:
    day = "Неділя"


temp = customtkinter.CTkLabel(screen, text= f"{w_api_D.temp_present_celsius}°", width=79, height= 71, font= (custom_font, 79), text_color= "white")
weather_event = customtkinter.CTkLabel(screen, text = f"{w_api_D.weather_main}", text_color= "white", font= (custom_font, 33))
min = customtkinter.CTkLabel(screen, text = f"↓{w_api_D.min_temp_celsius}°",text_color= "white", font= (custom_font, 27))
max = customtkinter.CTkLabel(screen, text = f"↑{w_api_D.max_temp_celsius}°",text_color= "white", font= (custom_font, 27))




dnipro = customtkinter.CTkLabel(screen, text = "Дніпро",text_color= "white", font= (custom_font, 31))
kiiv = customtkinter.CTkLabel(screen, text = "Київ",text_color= "white", font= (custom_font, 31) )
rome =customtkinter.CTkLabel(screen, text = "Рим",text_color= "white", font= (custom_font, 31))
london = customtkinter.CTkLabel(screen, text = "Лондон",text_color= "white", font= (custom_font, 31) )
varshava = customtkinter.CTkLabel(screen, text = "Варшава",text_color= "white", font= (custom_font, 31) )
praga = customtkinter.CTkLabel(screen, text = "Прага", text_color= "white", font= (custom_font, 31))

weather_icon = customtkinter.CTkImage(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"),size = (171, 159))

if w_api_D.weather_main == "Безхмарно":
    weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"))

elif w_api_D.weather_main == "Хмарно":
    weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"))

elif w_api_D.weather_main == "Дощ":
    weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

elif w_api_D.weather_main == "Сніг":
    weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))


weather_icon_label = customtkinter.CTkLabel(screen, text = None, image= weather_icon) 


def switch_position1():
    global weather_icon_label

    event_dnipro.configure(bg_color = "#5DA7B1")
    min_max_temp_dnipro.configure(bg_color = "#5DA7B1")

    event_kyiv.configure(bg_color = "#096C82")
    min_max_temp_kyiv.configure(bg_color = "#096C82")

    event_rome.configure(bg_color = "#096C82")
    min_max_temp_rome.configure(bg_color = "#096C82")

    event_london.configure(bg_color = "#096C82")
    min_max_temp_london.configure(bg_color = "#096C82")

    event_warsaw.configure(bg_color = "#096C82")
    min_max_temp_warsaw.configure(bg_color = "#096C82")

    event_prague.configure(bg_color = "#096C82")
    min_max_temp_prague.configure(bg_color = "#096C82")


    temp_dnipro.configure(bg_color = "#5DA7B1")
    temp_kyiv.configure(bg_color = "#096C82")
    temp_rome.configure(bg_color = "#096C82")
    temp_london.configure(bg_color = "#096C82")
    temp_warsaw.configure(bg_color = "#096C82")
    temp_prague.configure(bg_color = "#096C82")
    
    time_label_dnipro.place(x = 1000, y = 265)
    date_label_dnipro.place(x = 950, y = 315)
    time_label_kyiv.place_forget()
    date_label_kyiv.place_forget()
    time_label_london.place_forget()
    date_label_london.place_forget()
    time_label_prague.place_forget()
    date_label_prague.place_forget()
    time_label_rome.place_forget()
    date_label_rome.place_forget()
    time_label_warsaw.place_forget()
    date_label_warsaw.place_forget()





    if w_api_D.weather_main == "Хмарно":

        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"))

    if w_api_D.weather_main == "Безхмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"))

    elif w_api_D.weather_main == "Хмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"))

    elif w_api_D.weather_main == "Дощ":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

    elif w_api_D.weather_main == "Сніг":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png")) 


    frame3.configure(fg_color = "#5DA7B1", hover_color = "#5DA7B1")
    label3.configure(fg_color = "#5DA7B1")

    frame4.configure(fg_color = "#096C82", hover_color= "#096C82")
    label4.configure(fg_color = "#096C82")

    frame5.configure(fg_color = "#096C82", hover_color= "#096C82")
    label5.configure(fg_color = "#096C82")

    frame6.configure(fg_color = "#096C82", hover_color= "#096C82")
    label6.configure(fg_color = "#096C82")

    frame7.configure(fg_color = "#096C82", hover_color= "#096C82")
    label7.configure(fg_color = "#096C82") 

    frame8.configure(fg_color = "#096C82", hover_color= "#096C82")
    label8.configure(fg_color = "#096C82")

    dnipro.place(x = 650, y = 170)
    kiiv.place_forget()
    rome.place_forget()
    london.place_forget()
    varshava.place_forget()
    praga.place_forget()

    temp.configure( text = f"{w_api_D.temp_present_celsius}°")
    # w_api_D.temp_present.place(x = 0, y = 0)
    min.configure( text= f"↓{w_api_D.temp_present_celsius}°")
    max.configure(text = f"↑{w_api_D.max_temp_celsius}°")
    weather_event.configure(text = f"{w_api_D.weather_main}")
    sunset_label.configure(text = f"Захід сонця о {w_api_D.sunset_time}")
    time_label_dnipro.configure(text = time_oclock_dnipro)

    return weather_icon



def switch_position2():
    global weather_icon_label


    event_dnipro.configure(bg_color = "#096C82")
    min_max_temp_dnipro.configure(bg_color = "#096C82")

    event_kyiv.configure(bg_color = "#5DA7B1")
    min_max_temp_kyiv.configure(bg_color = "#5DA7B1")

    event_rome.configure(bg_color = "#096C82")
    min_max_temp_rome.configure(bg_color = "#096C82")

    event_london.configure(bg_color = "#096C82")
    min_max_temp_london.configure(bg_color = "#096C82")

    event_warsaw.configure(bg_color = "#096C82")
    min_max_temp_warsaw.configure(bg_color = "#096C82")
    
    event_prague.configure(bg_color = "#096C82")
    min_max_temp_prague.configure(bg_color = "#096C82")

    temp_dnipro.configure(bg_color = "#096C82")
    temp_kyiv.configure(bg_color = "#5DA7B1")
    temp_rome.configure(bg_color = "#096C82")
    temp_london.configure(bg_color = "#096C82")
    temp_warsaw.configure(bg_color = "#096C82")
    temp_prague.configure(bg_color = "#096C82")
    
    time_label_dnipro.place_forget()
    date_label_dnipro.place_forget()
    time_label_kyiv.place(x = 1000, y = 265)
    date_label_kyiv.place(x = 950, y = 315)
    time_label_london.place_forget()
    date_label_london.place_forget()
    time_label_prague.place_forget()
    date_label_prague.place_forget()
    time_label_rome.place_forget()
    date_label_rome.place_forget()
    time_label_warsaw.place_forget()
    date_label_warsaw.place_forget()



    if w_api_K.weather_main == "Безхмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"))

    elif w_api_K.weather_main == "Хмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"))

    elif w_api_K.weather_main == "Дощ":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

    elif w_api_K.weather_main == "Сніг":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))


    frame3.configure(fg_color = "#096C82", hover_color= "#096C82")
    label3.configure(fg_color = "#096C82")

    frame4.configure(fg_color = "#5DA7B1", hover_color = "#5DA7B1")
    label4.configure(fg_color = "#5DA7B1")

    frame5.configure(fg_color = "#096C82", hover_color= "#096C82")
    label5.configure(fg_color = "#096C82")

    frame6.configure(fg_color = "#096C82", hover_color= "#096C82")
    label6.configure(fg_color = "#096C82")

    frame7.configure(fg_color = "#096C82", hover_color= "#096C82")
    label7.configure(fg_color = "#096C82")
    
    frame8.configure(fg_color = "#096C82", hover_color= "#096C82")
    label8.configure(fg_color = "#096C82")

    dnipro.place_forget()
    kiiv.place(x = 650, y = 170)
    rome.place_forget()
    london.place_forget()
    varshava.place_forget()
    praga.place_forget()

    temp.configure( text = f"{w_api_K.temp_present_celsius}°")
    temp.configure()
    min.configure( text= f"↓{w_api_K.temp_present_celsius}°")
    max.configure(text = f"↑{w_api_K.max_temp_celsius}°")
    weather_event.configure(text = f"{w_api_K.weather_main}")
    sunset_label.configure(text = f"Захід сонця о {w_api_K.sunset_time}")
    time_label_kyiv.configure(text = time_oclock_kyiv)

    return weather_icon

def switch_position3():

    event_dnipro.configure(bg_color = "#096C82")
    min_max_temp_dnipro.configure(bg_color = "#096C82")

    event_kyiv.configure(bg_color = "#096C82")
    min_max_temp_kyiv.configure(bg_color = "#096C82")

    event_rome.configure(bg_color = "#096C82")
    min_max_temp_rome.configure(bg_color = "#096C82")

    event_london.configure(bg_color = "#5DA7B1")
    min_max_temp_london.configure(bg_color = "#5DA7B1")

    event_warsaw.configure(bg_color = "#096C82")
    min_max_temp_warsaw.configure(bg_color = "#096C82")

    event_prague.configure(bg_color = "#096C82")
    min_max_temp_prague.configure(bg_color = "#096C82")




    time_label_dnipro.place_forget()
    date_label_dnipro.place_forget()
    time_label_kyiv.place_forget()
    date_label_kyiv.place_forget()
    time_label_rome.place(x = 1000, y = 265)
    date_label_rome.place(x = 950, y = 315)
    time_label_london.place_forget()
    date_label_london.place_forget()
    time_label_warsaw.place_forget()
    date_label_warsaw.place_forget()
    time_label_prague.place_forget()
    date_label_prague.place_forget()
    

    temp_dnipro.configure(bg_color = "#096C82")
    temp_kyiv.configure(bg_color = "#096C82")
    temp_rome.configure(bg_color = "#096C82")
    temp_london.configure(bg_color = "#5DA7B1")
    temp_warsaw.configure(bg_color = "#096C82")
    temp_prague.configure(bg_color = "#096C82")

    global weather_icon_label



    if w_api_L.weather_main == "Безхмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))

    elif w_api_L.weather_main == "Хмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"))

    elif w_api_L.weather_main == "Дощ":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

    elif w_api_L.weather_main == "Сніг":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))






    frame3.configure(fg_color = "#096C82", hover_color= "#096C82")
    label3.configure(fg_color = "#096C82")
    
    frame4.configure(fg_color = "#096C82", hover_color= "#096C82")
    label4.configure(fg_color = "#096C82")

    frame5.configure(fg_color = "#5DA7B1", hover_color = "#5DA7B1")
    label5.configure(fg_color = "#5DA7B1")

    frame6.configure(fg_color = "#096C82", hover_color= "#096C82")
    label6.configure(fg_color = "#096C82")

    frame7.configure(fg_color = "#096C82", hover_color= "#096C82")
    label7.configure(fg_color = "#096C82")

    frame8.configure(fg_color = "#096C82", hover_color= "#096C82")
    label8.configure(fg_color = "#096C82")


    dnipro.place_forget()
    kiiv.place_forget()
    rome.place(x = 650, y = 170)
    london.place_forget()
    varshava.place_forget()
    praga.place_forget()

    temp.configure( text = f"{w_api_L.temp_present_celsius}°")
    min.configure( text= f"↓{w_api_L.temp_present_celsius}°")
    max.configure(text = f"↑{w_api_L.max_temp_celsius}°")
    weather_event.configure(text = f"{w_api_L.weather_main}")
    sunset_label.configure(text = f"Захід сонця о {w_api_L.sunset_time}")
    time_label_london.configure(text = time_oclock_london)

    return weather_icon

def switch_position4():
    global weather_icon_label
    
    event_dnipro.configure(bg_color = "#096C82")
    min_max_temp_dnipro.configure(bg_color = "#096C82")

    event_kyiv.configure(bg_color = "#096C82")
    min_max_temp_kyiv.configure(bg_color = "#096C82")

    event_rome.configure(bg_color = "#096C82")
    min_max_temp_rome.configure(bg_color = "#096C82")

    event_london.configure(bg_color = "#096C82")
    min_max_temp_london.configure(bg_color = "#096C82")

    event_warsaw.configure(bg_color = "#096C82")
    min_max_temp_warsaw.configure(bg_color = "#096C82")
    
    event_prague.configure(bg_color = "#5DA7B1")
    min_max_temp_prague.configure(bg_color = "#5DA7B1")

    time_label_dnipro.place_forget()
    date_label_dnipro.place_forget()
    time_label_kyiv.place_forget()
    date_label_kyiv.place_forget()
    time_label_rome.place_forget()
    date_label_rome.place_forget()
    time_label_london.place(x = 1000, y = 265)
    date_label_london.place(x = 950, y = 315)
    time_label_warsaw.place_forget()
    date_label_warsaw.place_forget()
    time_label_prague.place_forget()
    date_label_prague.place_forget()





    temp_dnipro.configure(bg_color = "#096C82")
    temp_kyiv.configure(bg_color = "#096C82")
    temp_rome.configure(bg_color = "#096C82")
    temp_london.configure(bg_color = "#096C82")
    temp_warsaw.configure(bg_color = "#096C82")
    temp_prague.configure(bg_color = "#5DA7B1")



    if w_api_P.weather_main == "Безхмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"))

    elif w_api_P.weather_main == "Хмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"))

    elif w_api_P.weather_main == "Дощ":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

    elif w_api_P.weather_main == "Сніг":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))






    frame3.configure(fg_color = "#096C82", hover_color= "#096C82")
    label3.configure(fg_color = "#096C82")

    frame4.configure(fg_color = "#096C82", hover_color= "#096C82")
    label4.configure(fg_color = "#096C82")

    frame5.configure(fg_color = "#096C82", hover_color= "#096C82")
    label5.configure(fg_color = "#096C82")

    frame6.configure(fg_color = "#5DA7B1", hover_color = "#5DA7B1")
    label6.configure(fg_color = "#5DA7B1")

    frame7.configure(fg_color = "#096C82", hover_color= "#096C82")
    label7.configure(fg_color = "#096C82")

    frame8.configure(fg_color = "#096C82", hover_color= "#096C82")
    label8.configure(fg_color = "#096C82")


    dnipro.place_forget()
    kiiv.place_forget()
    rome.place_forget()
    london.place(x = 650, y = 170)
    varshava.place_forget()
    praga.place_forget()

    temp.configure( text = f"{w_api_P.temp_present_celsius}°")
    min.configure( text= f"↓{w_api_P.temp_present_celsius}°")
    max.configure(text = f"↑{w_api_P.max_temp_celsius}°")
    weather_event.configure(text = f"{w_api_P.weather_main}")
    sunset_label.configure(text = f"Захід сонця о {w_api_P.sunset_time}")
    time_label_prague.configure(text = time_oclock_prague)

    return weather_icon

def switch_position5():
    global weather_icon_label

    event_dnipro.configure(bg_color = "#096C82")
    min_max_temp_dnipro.configure(bg_color = "#096C82")

    event_kyiv.configure(bg_color = "#096C82")
    min_max_temp_kyiv.configure(bg_color = "#096C82")

    event_rome.configure(bg_color = "#5DA7B1")
    min_max_temp_rome.configure(bg_color = "#5DA7B1")

    event_london.configure(bg_color = "#096C82")
    min_max_temp_london.configure(bg_color = "#096C82")

    event_warsaw.configure(bg_color = "#096C82")
    min_max_temp_warsaw.configure(bg_color = "#096C82")
    
    event_prague.configure(bg_color = "#096C82")
    min_max_temp_prague.configure(bg_color = "#096C82")

    time_label_dnipro.place_forget()
    date_label_dnipro.place_forget()
    time_label_kyiv.place_forget()
    date_label_kyiv.place_forget()
    time_label_rome.place_forget()
    date_label_rome.place_forget()
    time_label_london.place_forget()
    date_label_london.place_forget()
    time_label_warsaw.place(x = 1000, y = 265)
    date_label_warsaw.place(x = 950, y = 315)
    time_label_prague.place_forget()
    date_label_prague.place_forget()    




    temp_dnipro.configure(bg_color = "#096C82")
    temp_kyiv.configure(bg_color = "#096C82")
    temp_rome.configure(bg_color = "#5DA7B1")
    temp_london.configure(bg_color = "#096C82")
    temp_warsaw.configure(bg_color = "#096C82")
    temp_prague.configure(bg_color = "#096C82")



    if w_api_R.weather_main == "Безхмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"))

    elif w_api_R.weather_main == "Хмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"))

    elif w_api_R.weather_main == "Дощ":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

    elif w_api_R.weather_main == "Сніг":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))








    frame3.configure(fg_color = "#096C82", hover_color= "#096C82")
    label3.configure(fg_color = "#096C82")

    frame4.configure(fg_color = "#096C82", hover_color= "#096C82")
    label4.configure(fg_color = "#096C82")

    frame5.configure(fg_color = "#096C82", hover_color= "#096C82")
    label5.configure(fg_color = "#096C82")

    frame6.configure(fg_color = "#096C82", hover_color= "#096C82")
    label6.configure(fg_color = "#096C82")

    frame7.configure(fg_color = "#5DA7B1", hover_color = "#5DA7B1")
    label7.configure(fg_color = "#5DA7B1")

    frame8.configure(fg_color = "#096C82", hover_color= "#096C82")
    label8.configure(fg_color = "#096C82")


    dnipro.place_forget()
    kiiv.place_forget()
    rome.place_forget()
    london.place_forget()
    varshava.place(x = 650, y = 170)
    praga.place_forget()


    temp.configure( text = f"{w_api_R.temp_present_celsius}°")
    min.configure( text= f"↓{w_api_R.temp_present_celsius}°")
    max.configure(text = f"↑{w_api_R.max_temp_celsius}°")
    weather_event.configure(text = f"{w_api_R.weather_main}")
    sunset_label.configure(text = f"Захід сонця о {w_api_R.sunset_time}")
    time_label_rome.configure(text = time_oclock_rome)

    return weather_icon

def switch_position6():
    global weather_icon_label

    event_dnipro.configure(bg_color = "#096C82")
    min_max_temp_dnipro.configure(bg_color = "#096C82")

    event_kyiv.configure(bg_color = "#096C82")
    min_max_temp_kyiv.configure(bg_color = "#096C82")

    event_rome.configure(bg_color = "#096C82")
    min_max_temp_rome.configure(bg_color = "#096C82")

    event_london.configure(bg_color = "#096C82")
    min_max_temp_london.configure(bg_color = "#096C82")

    event_warsaw.configure(bg_color = "#5DA7B1")
    min_max_temp_warsaw.configure(bg_color = "#5DA7B1")
    
    event_prague.configure(bg_color = "#096C82")
    min_max_temp_prague.configure(bg_color = "#096C82")



    time_label_dnipro.place_forget()
    date_label_dnipro.place_forget()
    time_label_kyiv.place_forget()
    date_label_kyiv.place_forget()
    time_label_rome.place_forget()
    date_label_rome.place_forget()
    time_label_london.place_forget()
    date_label_london.place_forget()
    time_label_warsaw.place_forget()
    date_label_warsaw.place_forget()
    time_label_prague.place(x = 1000, y = 265)
    date_label_prague.place(x = 950, y = 315) 




    temp_dnipro.configure(bg_color = "#096C82")
    temp_kyiv.configure(bg_color = "#096C82")
    temp_rome.configure(bg_color = "#096C82")
    temp_london.configure(bg_color = "#096C82")
    temp_warsaw.configure(bg_color = "#5DA7B1")
    temp_prague.configure(bg_color = "#096C82")



    if w_api_W.weather_main == "Безхмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"))

    elif w_api_W.weather_main == "Хмарно":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412798.png"))

    elif w_api_W.weather_main == "Дощ":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

    elif w_api_W.weather_main == "Сніг":
        weather_icon.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))







    frame3.configure(fg_color = "#096C82", hover_color= "#096C82")
    label3.configure(fg_color = "#096C82")

    frame4.configure(fg_color = "#096C82", hover_color= "#096C82")
    label4.configure(fg_color = "#096C82")

    frame5.configure(fg_color = "#096C82", hover_color= "#096C82")
    label5.configure(fg_color = "#096C82")

    frame6.configure(fg_color = "#096C82", hover_color= "#096C82")
    label6.configure(fg_color = "#096C82")

    frame7.configure(fg_color = "#096C82", hover_color= "#096C82")
    label7.configure(fg_color = "#096C82")

    frame8.configure(fg_color = "#5DA7B1", hover_color = "#5DA7B1")
    label8.configure(fg_color = "#5DA7B1")


    dnipro.place_forget()
    kiiv.place_forget()
    rome.place_forget()
    london.place_forget()
    varshava.place_forget()
    praga.place(x = 650, y = 170)

    temp.configure( text = f"{w_api_W.temp_present_celsius}°")
    min.configure( text= f"↓{w_api_W.temp_present_celsius}°")
    max.configure(text = f"↑{w_api_W.max_temp_celsius}°")
    weather_event.configure(text = f"{w_api_W.weather_main}")
    sunset_label.configure(text = f"Захід сонця о {w_api_W.sunset_time}")
    time_label_warsaw.configure(text = time_oclock_warsaw)

    return weather_icon

position = customtkinter.CTkLabel(screen, text = "Поточна позиція", font = (custom_font, 61))

frame3 = customtkinter.CTkButton(screen, width= 236, height= 101, border_color= "white",  fg_color= "#5DA7B1", corner_radius= 20, border_width= 2, bg_color="#096C82", text= None, command = switch_position1, hover_color= "#5DA7B1" )
label3 = customtkinter.CTkLabel(screen,text = "Дніпро", text_color= "white")

frame4 = customtkinter.CTkButton(screen, width= 236, height= 101, border_color= "white",  fg_color= "#096C82", corner_radius= 20, border_width= 2, bg_color="#096C82", text= None, command = switch_position2, hover_color= "#096C82")
label4 = customtkinter.CTkLabel(screen,text = "Київ", text_color= "white", fg_color= "#096C82")

frame5 = customtkinter.CTkButton(screen, width= 236, height= 101, border_color= "white",  fg_color= "#096C82", corner_radius= 20, border_width= 2, bg_color="#096C82", text= None, command = switch_position3, hover_color= "#096C82" )
label5 = customtkinter.CTkLabel(screen,text = "Рим", text_color= "white", fg_color= "#096C82")

frame6 = customtkinter.CTkButton(screen, width= 236, height= 101, border_color= "white",  fg_color= "#096C82", corner_radius= 20, border_width= 2, bg_color="#096C82", text= None, command = switch_position4, hover_color= "#096C82" )
label6 = customtkinter.CTkLabel(screen,text = "Лондон", text_color= "white", fg_color= "#096C82")

frame7 = customtkinter.CTkButton(screen, width= 236, height= 101, border_color= "white",  fg_color= "#096C82", corner_radius= 20, border_width= 2, bg_color="#096C82", text= None, command = switch_position5, hover_color= "#096C82")
label7 = customtkinter.CTkLabel(screen,text = "Варшава", text_color= "white", fg_color= "#096C82")

frame8 = customtkinter.CTkButton(screen, width= 236, height= 101, border_color= "white",  fg_color= "#096C82", corner_radius= 20, border_width= 2, bg_color="#096C82", text= None, command = switch_position6, hover_color= "#096C82" )
label8 = customtkinter.CTkLabel(screen,text = "Прага", text_color= "white", fg_color= "#096C82")


date_label_dnipro = customtkinter.CTkLabel(screen, text = date_dnipro, font = (custom_font, 35), text_color= "white")
date_label_kyiv = customtkinter.CTkLabel(screen, text = date_kyiv, font = (custom_font, 35), text_color= "white")
date_label_london = customtkinter.CTkLabel(screen, text = date_london, font = (custom_font, 35), text_color= "white")
date_label_prague = customtkinter.CTkLabel(screen, text = date_prague, font = (custom_font, 35), text_color= "white")
date_label_rome = customtkinter.CTkLabel(screen, text = date_rome, font = (custom_font, 35), text_color= "white")
date_label_warsaw = customtkinter.CTkLabel(screen, text = date_warsaw, font = (custom_font, 35), text_color= "white")

time_label_dnipro = customtkinter.CTkLabel(screen, text = now_dnipro, font = (custom_font, 35), text_color= "white")
time_label_kyiv = customtkinter.CTkLabel(screen, text = now_kyiv, font = (custom_font, 35), text_color= "white")
time_label_london = customtkinter.CTkLabel(screen, text = now_london, font = (custom_font, 35), text_color= "white")
time_label_prague = customtkinter.CTkLabel(screen, text = now_prague, font = (custom_font, 35), text_color= "white")
time_label_rome = customtkinter.CTkLabel(screen, text = now_rome, font = (custom_font, 35), text_color= "white")
time_label_warsaw = customtkinter.CTkLabel(screen, text = now_warsaw, font = (custom_font, 35), text_color= "white")

day_label = customtkinter.CTkLabel(screen, text = day, font = (custom_font, 35), text_color= "white")



frame9 = customtkinter.CTkFrame(screen, width= 818, height= 240, corner_radius= 20, border_color= "white", border_width= 5, fg_color= "#5DA7B1")
frame10 = customtkinter.CTkFrame(screen, width = 818, height = 4,  fg_color= "white")
sunset_label = customtkinter.CTkLabel(screen, text = f"Захід сонця о {w_api_D.sunset_time}",text_color= "white", font= (custom_font, 27))

label11 = customtkinter.CTkLabel(screen, text = "Зараз",text_color= "white", font= (custom_font, 31))



now_dnipro = datetime.now(pytz.timezone(ukraine_timezone))
time_update_dnipro= now_dnipro.strftime("%H:%M")
time_label_dnipro.configure(text = time_update_dnipro)

now_kyiv = datetime.now(pytz.timezone(ukraine_timezone))
time_update_kyiv = now_kyiv.strftime("%H:%M")
time_label_kyiv.configure(text = time_update_kyiv)

now_london = datetime.now(pytz.timezone(london_timezone))
time_update_london = now_london.strftime("%H:%M")
time_label_london.configure(text = time_update_london)

now_prague = datetime.now(pytz.timezone(prague_timezone))
time_update_prague = now_prague.strftime("%H:%M")
time_label_prague.configure(text = time_update_prague)

now_rome = datetime.now(pytz.timezone(rome_timezone))
time_update_rome = now_rome.strftime("%H:%M")
time_label_rome.configure(text = time_update_rome)

now_warsaw = datetime.now(pytz.timezone(warsaw_timezone))
time_update_warsaw = now_warsaw.strftime("%H:%M")
time_label_warsaw.configure(text = time_update_warsaw)

forecast_img1 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52))
forecast_img2 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52)) 
forecast_img3 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52))
forecast_img4 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52)) 
forecast_img5 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52))
forecast_img6 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52)) 
forecast_img7 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52))
forecast_img8 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52)) 
forecast_img9 = customtkinter.CTkImage(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412794.png"), size = (50, 52))


forecast_img_label1 = customtkinter.CTkLabel(screen, image = forecast_img1, text = " ", width = 50, height = 52)
forecast_img_label2 = customtkinter.CTkLabel(screen, image = forecast_img2, text = " ", width = 50, height = 52)
forecast_img_label3 = customtkinter.CTkLabel(screen, image = forecast_img3, text = " ", width = 50, height = 52)
forecast_img_label4 = customtkinter.CTkLabel(screen, image = forecast_img4, text = " ", width = 50, height = 52)
forecast_img_label5 = customtkinter.CTkLabel(screen, image = forecast_img5, text = " ", width = 50, height = 52)
forecast_img_label6 = customtkinter.CTkLabel(screen, image = forecast_img6, text = " ", width = 50, height = 52)
forecast_img_label7 = customtkinter.CTkLabel(screen, image = forecast_img7, text = " ", width = 50, height = 52)
forecast_img_label8 = customtkinter.CTkLabel(screen, image = forecast_img8, text = " ", width = 50, height = 52)
forecast_img_label9 = customtkinter.CTkLabel(screen, image = forecast_img9, text = " ", width = 50, height = 52)

if F_W_D.list_events[0] == "Хмарно":
    forecast_img1.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412798.png"))
elif F_W_D.list_events[0] == "Сніг":
    forecast_img1.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))
elif F_W_D.list_events[0] == "Безхмарно":
    forecast_img1.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))
elif F_W_D.list_events[0] == "Дощ":
    forecast_img1.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

if F_W_D.list_events[1] == "Хмарно":
    forecast_img2.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412798.png"))
elif F_W_D.list_events[1] == "Сніг":
    forecast_img2.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))
elif F_W_D.list_events[1] == "Безхмарно":
    forecast_img2.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))
elif F_W_D.list_events[1] == "Дощ":
    forecast_img2.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

if F_W_D.list_events[2] == "Хмарно":
    forecast_img3.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412798.png"))
elif F_W_D.list_events[2] == "Сніг":
    forecast_img3.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))
elif F_W_D.list_events[2] == "Безхмарно":
    forecast_img3.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))
elif F_W_D.list_events[2] == "Дощ":
    forecast_img3.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

if F_W_D.list_events[3] == "Хмарно":
    forecast_img4.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412798.png"))
elif F_W_D.list_events[3] == "Сніг":
    forecast_img4.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))
elif F_W_D.list_events[3] == "Безхмарно":
    forecast_img4.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))
elif F_W_D.list_events[3] == "Дощ":
    forecast_img4.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

if F_W_D.list_events[4] == "Хмарно":
    forecast_img5.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412798.png"))
elif F_W_D.list_events[4] == "Сніг":
    forecast_img5.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))
elif F_W_D.list_events[4] == "Безхмарно":
    forecast_img5.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))
elif F_W_D.list_events[4] == "Дощ":
    forecast_img5.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

if F_W_D.list_events[5] == "Хмарно":
    forecast_img7.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412798.png"))
elif F_W_D.list_events[5] == "Сніг":
    forecast_img6.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))
elif F_W_D.list_events[5] == "Безхмарно":
    forecast_img6.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))
elif F_W_D.list_events[5] == "Дощ":
    forecast_img6.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

if F_W_D.list_events[6] == "Хмарно":
    forecast_img7.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412798.png"))
elif F_W_D.list_events[6] == "Сніг":
    forecast_img7.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))
elif F_W_D.list_events[6] == "Безхмарно":
    forecast_img7.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))
elif F_W_D.list_events[6] == "Дощ":
    forecast_img7.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))

if F_W_D.list_events[7] == "Хмарно":
    forecast_img8.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images/sunny_2412798.png"))
elif F_W_D.list_events[7] == "Сніг":
    forecast_img8.configure(light_image = Image.open(r"C:\weather_app_4_team\modules\images\snowy_2412768.png"))
elif F_W_D.list_events[7] == "Безхмарно":
    forecast_img8.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\sunny_2412794.png"))
elif F_W_D.list_events[7] == "Дощ":
    forecast_img8.configure(light_image= Image.open(r"C:\weather_app_4_team\modules\images\rainy_2412747.png"))


forecast_img_label1.place(x = 350, y = 580)
forecast_img_label2.place(x = 450, y = 580)
forecast_img_label3.place(x = 550, y = 580)
forecast_img_label4.place(x = 650, y = 580)
forecast_img_label5.place(x = 750, y = 580)
forecast_img_label6.place(x = 850, y = 580)
forecast_img_label7.place(x = 950, y = 580)
forecast_img_label8.place(x = 1050, y = 580)

time1 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[0]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")
time2 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[1]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")
time3 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[2]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")
time4 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[3]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")
time5 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[4]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")
time6 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[5]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")
time7 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[6]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")
time8 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[7]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")
time9 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_time[8]}", width=51, height= 31, font= (custom_font, 18), text_color= "white")

temp1 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[0]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")
temp2 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[1]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")
temp3 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[2]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")
temp4 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[3]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")
temp5 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[4]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")
temp6 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[5]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")
temp7 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[6]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")
temp8 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[7]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")
temp9 = customtkinter.CTkLabel(screen, text= f"{F_W_D.list_temp[8]}°", width=41, height= 30, font= (custom_font, 30), text_color= "white")

temp_dnipro = customtkinter.CTkLabel(screen, text= f"{w_api_D.temp_present_celsius}°", width=49, height= 41, font= (custom_font, 40), text_color= "white")
temp_kyiv = customtkinter.CTkLabel(screen, text= f"{w_api_K.temp_present_celsius}°", width=49, height= 41, font= (custom_font, 40), text_color= "white", bg_color = "#096C82")
temp_rome = customtkinter.CTkLabel(screen, text= f"{w_api_R.temp_present_celsius}°", width=40, height= 41, font= (custom_font, 40), text_color= "white", bg_color = "#096C82")
temp_london = customtkinter.CTkLabel(screen, text= f"{w_api_L.temp_present_celsius}°", width=40, height= 41, font= (custom_font, 40), text_color= "white", bg_color= "#096C82")
temp_prague = customtkinter.CTkLabel(screen, text= f"{w_api_P.temp_present_celsius}°", width=40, height= 41, font= (custom_font, 40), text_color= "white", bg_color = "#096C82")
temp_warsaw = customtkinter.CTkLabel(screen, text= f"{w_api_W.temp_present_celsius}°", width=40, height= 41, font= (custom_font, 40), text_color= "white", bg_color = "#096C82")

min_max_temp_dnipro = customtkinter.CTkLabel(screen, text= f"мін.: {w_api_D.min_temp_celsius}°,макс.: {w_api_D.max_temp_celsius}°", width=104, height= 14, font= (custom_font, 12), text_color= "white")
min_max_temp_kyiv = customtkinter.CTkLabel(screen, text= f"мін.: {w_api_K.min_temp_celsius}°,макс.: {w_api_K.max_temp_celsius}°", width=104, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")
min_max_temp_rome = customtkinter.CTkLabel(screen, text= f"мін.: {w_api_R.min_temp_celsius}°,макс.: {w_api_R.max_temp_celsius}°", width=104, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")
min_max_temp_london = customtkinter.CTkLabel(screen, text= f"мін.: {w_api_L.min_temp_celsius}°,макс.: {w_api_L.max_temp_celsius}°", width=104, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")
min_max_temp_warsaw = customtkinter.CTkLabel(screen, text= f"мін.: {w_api_W.min_temp_celsius}°,макс.: {w_api_W.max_temp_celsius}°", width=104, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")
min_max_temp_prague = customtkinter.CTkLabel(screen, text= f"мін.: {w_api_K.min_temp_celsius}°,макс.: {w_api_K.max_temp_celsius}°", width=104, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")

event_dnipro = customtkinter.CTkLabel(screen, text= f"{w_api_D.weather_main}", width=52, height= 14, font= (custom_font, 12), text_color= "white")
event_kyiv = customtkinter.CTkLabel(screen, text= f"{w_api_K.weather_main}", width=52, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")
event_rome = customtkinter.CTkLabel(screen, text= f"{w_api_R.weather_main}", width=52, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")
event_london = customtkinter.CTkLabel(screen, text= f"{w_api_L.weather_main}", width=52, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")
event_warsaw = customtkinter.CTkLabel(screen, text= f"{w_api_W.weather_main}", width=52, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")
event_prague = customtkinter.CTkLabel(screen, text= f"{w_api_P.weather_main}", width=52, height= 14, font= (custom_font, 12), text_color= "white", bg_color = "#096C82")


def update_time():

    now_dnipro = datetime.now(pytz.timezone(ukraine_timezone))
    time_update_dnipro= now_dnipro.strftime("%H:%M")
    time_label_dnipro.configure(text = time_update_dnipro)
    
    now_kyiv = datetime.now(pytz.timezone(ukraine_timezone))
    time_update_kyiv = now_kyiv.strftime("%H:%M")
    time_label_kyiv.configure(text = time_update_kyiv)

    now_london = datetime.now(pytz.timezone(london_timezone))
    time_update_london = now_london.strftime("%H:%M")
    time_label_london.configure(text = time_update_london)

    now_prague = datetime.now(pytz.timezone(prague_timezone))
    time_update_prague = now_prague.strftime("%H:%M")
    time_label_prague.configure(text = time_update_prague)

    now_rome = datetime.now(pytz.timezone(rome_timezone))
    time_update_rome = now_rome.strftime("%H:%M")
    time_label_rome.configure(text = time_update_rome)

    now_warsaw = datetime.now(pytz.timezone(warsaw_timezone))
    time_update_warsaw = now_warsaw.strftime("%H:%M")
    time_label_warsaw.configure(text = time_update_warsaw)

    screen.after(1000, update_time)

update_time()


name_lastname = lastname_value.get()

personal_button = customtkinter.CTkButton(screen, text = "Особистий кабінет", font=custom_font, command= personal_area,border_color= "#FFFFFF", height=50, width= 282, fg_color= "#5DA7B1",text_color="white",corner_radius= 20, bg_color="#5DA7B1")


#time_label = customtkinter.CTkLabel(screen, text = time.struct_time.tm_wday, font= (custom_font, 47))



personal_icon = customtkinter.CTkImage(light_image= Image.open(r"C:\weather_app_4_team\modules\images\user_9970571.png"), size = (50, 50))

personal_icon_label = customtkinter.CTkLabel(screen, text = None, image= personal_icon) 

def call_funcs():

    frame_dekstop.deiconify()

    screen.deiconify()
    save_country()  
    save_town()
    save_name() 
    save_lastname()
    user_reg.destroy()
    frame1.place(x = 0, y = 0)
    personal_button.place(relx=0.5, rely=0.5, x = -280,y = -395)
    temp.place(x = 650, y = 200)
    weather_event.place(x = 640, y = 290)
    frame2.place(x = 0, y = 0)
    time_label_dnipro.place(x = 1000, y = 265)
    date_label_dnipro.place(x = 950, y = 315)
    day_label.place(x = 980, y = 220)
    min.place(x = 645, y = 330)
    max.place(x = 715, y = 330)
    
    weather_icon_label.place(x =  340, y = 225)

    temp_dnipro.place(x = 185, y = 40)
    min_max_temp_dnipro.place(x = 140, y = 100)
    event_dnipro.place(x = 18, y = 100)
    # time_dnipro_min.place(x = 200, y = 111)

    temp_kyiv.place(x = 200, y = 170)
    min_max_temp_kyiv.place(x = 140, y = 235)
    event_kyiv.place(x = 22, y = 235)

    temp_rome.place(x = 180, y = 300)
    min_max_temp_rome.place(x = 140, y = 365 )
    event_rome.place(x = 22, y = 365)

    temp_london.place(x = 180, y = 440)
    min_max_temp_london.place(x = 140, y = 495)
    event_london.place(x = 22, y = 495)
    
    temp_warsaw.place(x = 200, y = 575)
    min_max_temp_warsaw.place(x = 140, y = 625)
    event_warsaw.place(x = 22, y = 625)
    
    temp_prague.place(x = 200, y = 700)
    min_max_temp_prague.place(x = 140, y = 765)
    event_prague.place(x = 22, y = 765)
    

    frame3.place(x = 15, y = 25)
    label3.place(x = 22, y = 50)

    frame4.place(x = 15, y = 157)
    label4.place(x = 22, y = 170)

    frame5.place(x = 15, y = 421)
    label5.place(x = 22, y = 432)

    frame6.place(x = 15, y = 685)
    label6.place(x = 22, y = 698)

    frame7.place(x = 15, y = 289)
    label7.place(x = 22, y = 302)

    frame8.place(x = 15, y = 553)
    label8.place(x = 22, y = 576)


    frame9.place(x = 325, y = 473)
    frame10.place(x = 325, y = 523)
    sunset_label.place(x = 350, y = 485)

    dnipro.place(x = 650, y = 170)

    time1.place(x = 350, y = 550)
    time2.place(x = 450, y = 550)
    time3.place(x = 550, y = 550)
    time4.place(x = 650, y = 550)
    time5.place(x = 750, y = 550)
    time6.place(x = 850, y = 550)
    time7.place(x = 950, y = 550)
    time8.place(x = 1050, y = 550)

    temp1.place(x = 350, y = 638)
    temp2.place(x = 450, y = 638)
    temp3.place(x = 550, y = 638)
    temp4.place(x = 650, y = 638)
    temp5.place(x = 750, y = 638)
    temp6.place(x = 850, y = 638)
    temp7.place(x = 950, y = 638)
    temp8.place(x = 1050, y = 638)


    # label12.place(x = 325, y = 531)

    personal_icon_label.place(x = 280, y = 5)

save_button = customtkinter.CTkButton(user_reg, text="зберегти ",font=custom_font,command= call_funcs,border_color= "#FFFFFF", height=50, width= 100, fg_color= "#096C82",hover_color= "light grey",border_width= 3,text_color="white",corner_radius= 20)
save_button.place(relx=0.5, rely=0.5, x= -85, y=230,)

# area_image = customtkinter.CTkImage(dark_image= "modules/images/user_9970571")

# clear_label= customtkinter.CTkImage(dark_image= path.find_path_to_file("/sunny_2412798.png"), light_image= path.find_path_to_file("/sunny_2412798.png"))
# clouds_label = customtkinter.CTkImage(dark_image= "sunny_2412798.png", light_image= "sunny_2412798.png")
# rain_label = customtkinter.CTkImage(dark_image= "sunny_2412798.png", light_image= "sunny_2412798.png")
# snow_label = customtkinter.CTkImage(dark_image= "sunny_2412798.png", light_image= "sunny_2412798.png")
# if w_api.weather_main == "Clear":
#     clear_img = path.find_path_to_file("sunny_2412794.png")
# elif w_api.weather_main == "Clouds":
#     clouds_img = None
# elif w_api.weather_main == "Rain":
#     rain_img = None
# elif w_api.weather_main == "Snow":
#     snow_img = None

count = 0

def weather_all_day():
    pass
        # forecast_time1 = customtkinter.CTkLabel(text = "21:00", weight = 41, height = 27, bg_color = "#5DA7B1")
        # forecast_time1.place(x = 250, y = 400)
weather_all_day()

screen.mainloop()



