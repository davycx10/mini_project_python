import os
import random
from tkinter import * 

class Meals_genarate:
    def __init__(self):
        
        self.window = Tk()
        self.window.title("Interface pour le générateur de repas")
        self.window.geometry("720x480")
        self.window.config(background="#950101")
        
        
        
        self.frame = Frame(self.window, background="white")
        self.frame.pack(expand=YES)
        
        self.random_meal_title = Label(self.frame, text="Soupe", font=("Helvetica", 30), bg="#E9EA81", fg="black")
        
        self.button_choice()
        
        self.generate_random_meals()
        
        #self.widget()
       
    #def widget(self):
    #    self.create_title()    
    #    self.create_subtitle()
        
    #def create_title(self):
    #    create_title = Label(self.frame, text="repas proposer:", bg="#950101", font=("Helvitica", 25))
    #    create_title.pack(side="right", anchor="nw")
        
    #def create        
        
    def generate_random_meals(self):
    
            if os.path.exists("meals.txt"):
                with open("meals.txt", "r") as file :
                    
                    meals_random_choice = random.choice(file.readlines())
                    self.random_meal_title.config(text=meals_random_choice, font=("Arial", 20), bg="#950101")
                    
                    self.random_meal_title.pack(fill=X)
                   
                    
            else:
                print("le fichier est vide aucun repas à proposer")
                
    def button_choice(self):
        generate_choices_button = Button(self.frame, text="repas proposer", bg="#950101", command=self.generate_random_meals)
        generate_choices_button.pack(fill=X)            
                

                         

app = Meals_genarate()
app.window.mainloop()