from tkinter import *
import webbrowser

def open_davycx_github():
    webbrowser.open_new("https://github.com/davycx10")

#créer une première fenetre
window = Tk()

#personnaliser la fenêtre
window.title("My application")
window.geometry("1080x400")
window.minsize(480, 360)
window.config(background= "#520505")

#créer la frame
frame = Frame(window, bg="#520505")

#ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur l'application", font=("Arial", 28), bg="#520505", fg="white")
label_title.pack()

#ajouter un second texte
label_subtitle = Label(frame, text="Hello There", font=("Arial", 18), bg="#520505", fg="white")
label_subtitle.pack()


github_button = Button(frame, text="Ouvrir github", font=("Arial", 18), bg="white", fg="#520505", command=open_davycx_github)
github_button.pack(pady=25)

#ajouter
frame.pack(expand=YES)

#afficher la fenetre
window.mainloop()