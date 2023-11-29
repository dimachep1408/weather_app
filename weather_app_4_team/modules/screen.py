import customtkinter 
import frames

screen = customtkinter.CTk(fg_color= "#5DA7B1")
screen.title("big screen")
screen.geometry("1200x800")
user_reg = customtkinter.CTkToplevel(screen, fg_color="#5DA7B1")
user_reg.title("Реєстрація користувача")
user_reg.geometry("460x645")

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

label_lastname = customtkinter.CTkLabel(user_reg, text="Прізвище:", text_color= "white", font=custom_font)
label_lastname.place(relx=0.5, rely=0.5, x = -66, y =100 )
entry_lastname = customtkinter.CTkEntry(user_reg, fg_color = "#096C82",  corner_radius= 20,border_width = 5, border_color="#FFFFFF",height=46, width= 218)
entry_lastname.place(relx=0.5, rely=0.5, x = -77 , y = 150)

lastname_value = customtkinter.StringVar()
def save_lastname():
    value = entry_lastname.get()
    lastname_value.set(value)
    print("Прізвище:", lastname_value.get())
def personal_area():
    
    label_country_reg = customtkinter.CTkLabel(user_reg, text= country_value, text_color= "green")
    label_country_reg.place(x = -45 , y = -150)
    # save_button.place(relx=0.5, rely=0.5, x=200, y=120)


personal_button = customtkinter.CTkButton(screen, text="Лічний кабінет ",font=custom_font, command= personal_area(),border_color= "#FFFFFF", height=50, width= 100, fg_color= "#096C82",hover_color= "#096C82",border_width= 5,text_color="white",corner_radius= 20)


def call_funcs():
    save_country()  
    save_town()
    save_name() 
    save_lastname()
    user_reg.destroy()
    personal_button.place(relx=0.5, rely=0.5, x = -600,y = -400)


save_button = customtkinter.CTkButton(user_reg, text="зберегти ",font=custom_font,command= call_funcs,border_color= "#FFFFFF", height=50, width= 100, fg_color= "#096C82",hover_color= "light grey",border_width= 3,text_color="white",corner_radius= 20)
save_button.place(relx=0.5, rely=0.5, x= -30, y=200,)



