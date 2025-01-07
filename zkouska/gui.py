import tkinter as tk

# Vytvoření hlavního okna
okno = tk.Tk()
okno.title("Moje první GUI aplikace")  # Nastavení názvu okna
okno.geometry("500x200")  # Nastavení velikosti okna

# Přidání štítku (textového pole)
label = tk.Label(okno, text="Ja se to naucim!", font=("Times new roman", 14))
label.pack(pady=20)  # Umístění do okna s odsazením

# Funkce, která se spustí po kliknutí na tlačítko
def klik_na_tlacitko():
    label.config(text="Tlačítko bylo stisknuto!")

# Přidání tlačítka
tlacitko = tk.Button(okno, text="Klikni na mě", command=klik_na_tlacitko)
tlacitko.pack()

# Spuštění aplikace
okno.mainloop()

