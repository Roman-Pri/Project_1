import tkinter as tk

# Příklad funkce pro zobrazení textu
def zobrazit_vysledky():
    # Vytvoření hlavního okna
    root = tk.Tk()
    root.title("Výsledky turnaje")

    # Vytvoření Text widgetu
    text_widget = tk.Text(root, height=20, width=50)
    text_widget.pack()

    # Ukázkové hodnoty
    celkova_cena_za_turnaj = 5000
    vysledky_text = f"Celková cena za celý turnaj: {celkova_cena_za_turnaj} Kč\n"

    # Vložení textu do widgetu
    text_widget.insert(tk.END, vysledky_text)

    # Konfigurace tagů pro formátování
    text_widget.tag_configure("bold", font=("Arial", 10, "bold"))
    text_widget.tag_configure("red", foreground="red")

    # Najdeme text "Celková cena za celý turnaj"
    start_index = text_widget.search("Celková cena za celý turnaj", "1.0", stopindex=tk.END)
    if start_index:
        end_index = text_widget.index(f"{start_index}+{len('Celková cena za celý turnaj')}c")
        text_widget.tag_add("bold", start_index, end_index)  # Tučný text
        text_widget.tag_add("red", start_index, end_index)   # Červený text

    # Najdeme hodnotu celkove_cena_za_turnaj a zvýrazníme ji
    start_index = text_widget.index(f"{end_index}+1c")
    end_index = text_widget.index(f"{start_index}+{len(str(celkova_cena_za_turnaj))}c")
    text_widget.tag_add("bold", start_index, end_index)  # Tučný text
    text_widget.tag_add("red", start_index, end_index)   # Červený text

    # Spuštění hlavní smyčky
    root.mainloop()

# Zavolání funkce pro zobrazení výsledků
zobrazit_vysledky()