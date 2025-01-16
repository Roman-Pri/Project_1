"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Ing. Roman Příhonský, MMS, MSS
email:  roman.prihonsky83@gmail.com
"""
# Intial data
import random           # podpora pro tvorbu nahodneho cisla
import datetime         # podpora pro mereni delky hry
import tkinter          # GUI
import pandas as pd     # uchovani statistik
import matplotlib       # zobrazeni statistik

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
button = tkinter.Button(window, text = "NEW GAME", font = ("Arial", 20), width = 15, height= 2) #chybi definovat command (command = button_click)
button.place(x = 525, y = 200)

# 1.4 button "GS"
button = tkinter.Button(window, text = "GAME STATISTICS", font = ("Arial", 20), width = 15, height= 2) #chybi definovat command (command = button_click)
button.place(x = 525, y = 350)

# 1.5 button "Opt"
button = tkinter.Button(window, text = "OPTIONS", font = ("Arial", 20), width = 15, height= 2) #chybi definovat command (command = button_click)
button.place(x = 525, y = 500)

window.mainloop()