import customtkinter 

class Add_screen (customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Weather")
        self.geometry("400x400")  
        self.h("Green")   
screen = Add_screen()
screen.mainloop()