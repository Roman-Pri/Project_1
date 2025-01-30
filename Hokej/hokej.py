import tkinter as tk
import random
import os  # pro kontrolu existence souboru

# Funkce pro rozdělení hráčů do dvou týmů
def rozdelit_tymy(hraci):
    random.shuffle(hraci)
    polovina = len(hraci) // 2
    tym1 = hraci[:polovina]
    tym2 = hraci[polovina:]
    return tym1, tym2

# Funkce pro uložení týmů do souboru
def ulozit_do_souboru(tym1, tym2):
    with open("tymy.txt", "w", encoding="utf-8") as soubor:  # Otevření souboru s kódováním utf-8
        soubor.write("Tým 1:\n")
        soubor.write("\n".join(tym1) + "\n\n")
        soubor.write("Tým 2:\n")
        soubor.write("\n".join(tym2) + "\n")
    print("Týmy byly uloženy do souboru 'tymy.txt'.")

# Funkce pro načtení hráčů ze souboru
def nacti_hrace():
    if os.path.exists("hraci.txt"):  # Zkontrolujeme, zda soubor existuje
        with open("hraci.txt", "r", encoding="utf-8") as soubor:
            hraci = soubor.read().splitlines()
        return hraci
    else:
        print("Soubor 'hraci.txt' neexistuje.")
        return []

# Funkce pro zobrazení rozdělených týmů v GUI
def zobrazit_rozdelene_tymy(entry_hraci):
    hraci = nacti_hrace()

    if not hraci:
        return

    tym1, tym2 = rozdelit_tymy(hraci)
    
    # Vytvoření okna pro zobrazení týmů
    okno = tk.Tk()
    okno.title("Rozdělené týmy")
    
    # Zobrazení týmů
    label_tym1 = tk.Label(okno, text="Tým 1:\n" + "\n".join(tym1), font=("Arial", 12), justify="left")
    label_tym1.pack(pady=10)
    label_tym2 = tk.Label(okno, text="Tým 2:\n" + "\n".join(tym2), font=("Arial", 12), justify="left")
    label_tym2.pack(pady=10)

    # Uložení týmů do souboru
    ulozit_do_souboru(tym1, tym2)

    okno.mainloop()

# Funkce pro přidání nových hráčů do souboru
def pridat_hrace(entry_hraci):
    nove_hraci = entry_hraci.get().split(",")
    nove_hraci = [hrac.strip() for hrac in nove_hraci]  # Odstranění bílých znaků
    if nove_hraci:
        with open("hraci.txt", "a", encoding="utf-8") as soubor:
            for hrac in nove_hraci:
                soubor.write(hrac + "\n")
        print(f"Přidáno: {', '.join(nove_hraci)}")
        entry_hraci.delete(0, tk.END)  # Vyprázdnění textového pole
    else:
        print("Nejsou zadáni žádní hráči.")

# GUI setup
def hlavni_okno():
    window = tk.Tk()
    window.title("Rozdělení hráčů do týmů")
    
    # Textové pole pro zadání nových hráčů
    label = tk.Label(window, text="Zadejte jména hráčů (oddělená čárkou):", font=("Arial", 14))
    label.pack(pady=10)
    
    entry_hraci = tk.Entry(window, font=("Arial", 14), width=50)
    entry_hraci.pack(pady=10)
    
    # Tlačítko pro přidání hráčů do souboru
    button_pridat = tk.Button(window, text="Přidat hráče", font=("Arial", 14), command=lambda: pridat_hrace(entry_hraci))
    button_pridat.pack(pady=10)
    
    # Tlačítko pro rozdělení hráčů do týmů a zobrazení
    button_rozdelit = tk.Button(window, text="Rozdělit týmy", font=("Arial", 14), command=lambda: zobrazit_rozdelene_tymy(entry_hraci))
    button_rozdelit.pack(pady=10)
    
    window.mainloop()

# Spuštění hlavního okna
if __name__ == "__main__":
    hlavni_okno()
