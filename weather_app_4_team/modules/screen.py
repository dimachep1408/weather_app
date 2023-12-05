import customtkinter 
import weather_api as w_api
from datetime import datetime
import time
import find_file_path as path

screen = customtkinter.CTk(fg_color= "#5DA7B1")
screen.title("big screen")
screen.geometry("1200x800")
user_reg = customtkinter.CTkToplevel(screen, fg_color="#5DA7B1")
user_reg.title("Реєстрація користувача")
user_reg.geometry("460x645")

min_screen = customtkinter.CTk(fg_color= "#5DA7B1")
min_screen.title("mini screen")
min_screen.state( 'withdrawn')

custom_font = customtkinter.CTkFont(family ="Roboto Slab", size =28, weight ="bold")

label_country = customtkinter.CTkLabel(user_reg, text="Країна:", text_color= "white", font=custom_font)
label_country.place(relx=0.5, rely=0.5, x = -66, y =-200 )
entry_country = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 218)
entry_country.place(relx=0.5, rely=0.5, x = -77 , y = -150)

country_value = customtkinter.StringVar()

def save_country():
    value = entry_country.get()
    country_value.set(value)
    print("Країна:", country_value.get())

label_town = customtkinter.CTkLabel(user_reg, text="Місто:", text_color= "white", font=custom_font)
label_town.place(relx=0.5, rely=0.5, x = -66, y =-100 )
entry_town = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 218)
entry_town.place(relx=0.5, rely=0.5, x = -77 , y = -50)

town_value = customtkinter.StringVar()
def save_town():
    value = entry_town.get()
    town_value.set(value)
    print("Місто:", town_value.get())


label_name = customtkinter.CTkLabel(user_reg, text="Ім'я:", text_color= "white", font=custom_font)
label_name.place(relx=0.5, rely=0.5, x = -66, y =0  )
entry_name = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 218)
entry_name.place(relx=0.5, rely=0.5, x = -77 , y = 50)

name_value = customtkinter.StringVar()
def save_name():
    value = entry_name.get()
    name_value.set(value)
    print("Ім'я:", name_value.get())

label_lastname = customtkinter.CTkLabel(user_reg, text="Прізвище:", text_color= "white", font=custom_font, )
label_lastname.place(relx=0.5, rely=0.5, x = -66, y =100 )
entry_lastname = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 218)
entry_lastname.place(relx=0.5, rely=0.5, x = -77 , y = 150)

lastname_value = customtkinter.StringVar()
def save_lastname():
    value = entry_lastname.get()
    lastname_value.set(value)
    print("Прізвище:", lastname_value.get())

def close_reg():
    personal_button.configure(screen, text="Особистий кабінет ",font=custom_font, command= personal_area,border_color= "#FFFFFF", height=50, width= 282, fg_color= "#5DA7B1",text_color="white",corner_radius= 20, bg_color="#5DA7B1")
    label_country_reg.place_forget()
    label_town_reg.place_forget()
    label_name.place_forget()
    label_lastname.place_forget()
    label_country.place_forget()
    label_lastname_reg.place_forget()
    label_name_reg.place_forget()
    label_town.place_forget()

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

    label_country.place(relx=0.5, rely=0.5, x = -66, y =-200 )
    label_town.place(relx=0.5, rely=0.5, x = -66, y =-100 )
    label_name.place(relx=0.5, rely=0.5, x = -66, y =0  )
    label_lastname.place(relx=0.5, rely=0.5, x = -66, y =100 )

    personal_button.configure(screen, text="повернутися",font=custom_font, command= close_reg,border_color= "#FFFFFF", height=50, width= 282, fg_color= "#5DA7B1",text_color="white",corner_radius= 20, bg_color="#5DA7B1")
    # save_button.place(relx=0.5, rely=0.5, x=200, y=120)
    



frame1 = customtkinter.CTkFrame(screen, width= 1200, height= 800, border_color= "#096C82",  fg_color= "#5DA7B1", corner_radius= 20, border_width= 5 )
frame2 = customtkinter.CTkFrame(screen, width= 275, height= 800, border_color= "#096C82",  fg_color= "#096C82", corner_radius= 20, border_width= 5 )


now = datetime.now()
date = now.strftime("%d/%m/%Y")
time_oclock = now.strftime("%H:%M")
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
    day = "Воскресіня"


temp = customtkinter.CTkLabel(screen, text= w_api.temp_present_celsius, width=79, height= 71, font= (custom_font, 79), text_color= "white")
weather_event = customtkinter.CTkLabel(screen, text = w_api.weather_main, text_color= "white", font= (custom_font, 33))
gradus = customtkinter.CTkLabel(screen, text = "o", font= custom_font, text_color= "white")

date_label = customtkinter.CTkLabel(screen, text = date, font = (custom_font, 35), text_color= "white")
time_label = customtkinter.CTkLabel(screen, text = time_oclock, font = (custom_font, 35), text_color= "white")
day_label = customtkinter.CTkLabel(screen, text = day, font = (custom_font, 35), text_color= "white")
# day_week = customtkinter.CTkLabel(screen, text = day, font = (custom_font, 35), text_color= "white")

def update_time():
    now = datetime.now()
    time_update = now.strftime("%H:%M")
    time_label.configure(text = time_update)
    screen.after(1000, update_time)
update_time()

personal_button = customtkinter.CTkButton(screen, text="Особистий кабінет ",font=custom_font, command= personal_area,border_color= "#FFFFFF", height=50, width= 282, fg_color= "#5DA7B1",text_color="white",corner_radius= 20, bg_color="#5DA7B1")


#time_label = customtkinter.CTkLabel(screen, text = time.struct_time.tm_wday, font= (custom_font, 47))
def call_funcs():
    save_country()  
    save_town()
    save_name() 
    save_lastname()
    user_reg.destroy()
    frame1.place(x = 0, y = 0)
    personal_button.place(relx=0.5, rely=0.5, x = -280,y = -395)
    temp.place(x = 750, y = 250)
    gradus.place(x = 830, y = 255)
    weather_event.place(x = 730, y = 340)
    frame2.place(x = 0, y = 0)
    time_label.place(x = 1000, y = 265)
    date_label.place(x = 950, y = 315)
    day_label.place(x = 980, y = 220)

save_button = customtkinter.CTkButton(user_reg, text="зберегти ",font=custom_font,command= call_funcs,border_color= "#FFFFFF", height=50, width= 100, fg_color= "#096C82",hover_color= "light grey",border_width= 3,text_color="white",corner_radius= 20)
save_button.place(relx=0.5, rely=0.5, x= -30, y=200,)

# clear_label= customtkinter.CTkImage(dark_image= path.find_path_to_file("/sunny_2412798.png"), light_image= path.find_path_to_file("/sunny_2412798.png"))
# clouds_label = customtkinter.CTkImage(dark_image= "sunny_2412798.png", light_image= "sunny_2412798.png")
# rain_label = customtkinter.CTkImage(dark_image= "sunny_2412798.png", light_image= "sunny_2412798.png")
# snow_label = customtkinter.CTkImage(dark_image= "sunny_2412798.png", light_image= "sunny_2412798.png")
if w_api.weather_main == "Clear":
    clear_img = path.find_path_to_file("sunny_2412794.png")
elif w_api.weather_main == "Clouds":
    clouds_img = None
elif w_api.weather_main == "Rain":
    rain_img = None
elif w_api.weather_main == "Snow":
    snow_img = None



screen.mainloop()






