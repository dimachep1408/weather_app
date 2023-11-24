import customtkinter 
class Add_screen (customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Weather")
        self.geometry("1200x800")
        self.configure(bg="blue")
screen = Add_screen()
def button_event():
    label_country = customtkinter.CTkLabel(screen, text="Країна:", bg_color = "Green", text_color= "white")
    label_country.place(relx=0.5, rely=0.5, x = 5, y =-200 )
    entry_country = customtkinter.CTkEntry(screen, bg_color = "White")
    entry_country.place(relx=0.5, rely=0.5, x = -45 , y = -150)

    label_town = customtkinter.CTkLabel(screen, text="Місто:", bg_color = "Green", text_color= "white")
    label_town.place(relx=0.5, rely=0.5, x = 7, y =-100 )
    entry_town = customtkinter.CTkEntry(screen, bg_color = "White")
    entry_town.place(relx=0.5, rely=0.5, x = -45 , y = -50)

    label_name = customtkinter.CTkLabel(screen, text="Ім'я:", bg_color = "Green", text_color= "white")
    label_name.place(relx=0.5, rely=0.5, x = 12, y =0  )
    entry_name = customtkinter.CTkEntry(screen, bg_color = "White")
    entry_name.place(relx=0.5, rely=0.5, x = -45 , y = 50)

    label_lastname = customtkinter.CTkLabel(screen, text="Прізвище:", bg_color = "Green", text_color= "white")
    label_lastname.place(relx=0.5, rely=0.5, x = -7, y =100 )
    entry_lastname = customtkinter.CTkEntry(screen, bg_color = "White")
    entry_lastname.place(relx=0.5, rely=0.5, x = -45 , y = 150)

button = customtkinter.CTkButton(screen, text="Зареєструватись", command=button_event,border_color= "dark green", height=100, width= 250, fg_color= "grey",hover_color= "light grey",corner_radius = 5,text_color="green")
button.grid(padx = 500, pady = 500,)
button.place( x = 0, y = 0)





screen.mainloop()
