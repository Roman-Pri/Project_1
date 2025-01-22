"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Ing. Roman Příhonský, MMS, MSS
email:  roman.prihonsky83@gmail.com
"""
# Imported library
import random           # podpora pro tvorbu nahodneho cisla
import datetime         # podpora pro mereni delky hry
import tkinter          # GUI
import pandas           # uchovani statistik
import matplotlib       # zobrazeni statistik

# Functions definition
def run_new_game():
    for widget in window.winfo_children():
        widget.destroy()
    # opening label
    gra_for = "-" * 64
    opening_text_label = ("Hi there!\n" + 
        gra_for + 
        "\nI've generated a random 4 digit number for you.\n"
        "Let's play Bulls and Cows game.\n" +
        gra_for +
        "\nInsert the number and press Enter button:"
    )
    label = tkinter.Label(window, text = opening_text_label, font = ("Arial", 20), background = "green", justify = "left")
    label.place(x = 10, y = 10)
    # entry label
    entry = tkinter.Entry(window, font = ("Arial", 16), width = 10,)
    entry.place(x = 10, y = 220)
    # time label
    time_label = tkinter.Label(window, text="Game Time - 0:00", font=("Arial", 30), background = "green", justify = "right")
    time_label.place(x = 940, y = 10)
    
    
# 1.GUI
# 1.1 Window
window = tkinter.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Prepered by Roman Příhonský")
window.geometry(f"{screen_width}x{screen_height}")
window.configure(background = "green") 

# 1.2 Label
label = tkinter.Label(window, text = "Welcome to BULLs & COWs game", font = ("Arial", 40), background = "green")
label.pack(pady = 10)

# 1.3 button "NG"
button = tkinter.Button(window, text = "NEW GAME", font = ("Arial", 20), width = 15, height = 2, command = run_new_game) 
button.place(x = 525, y = 200)

# 1.4 button "GS"
button = tkinter.Button(window, text = "GAME STATISTICS", font = ("Arial", 20), width = 15, height= 2) #chybi definovat command (command = button_click)
button.place(x = 525, y = 350)

# 1.5 button "Opt"
button = tkinter.Button(window, text = "OPTIONS", font = ("Arial", 20), width = 15, height= 2) #chybi definovat command (command = button_click)
button.place(x = 525, y = 500)


window.mainloop()