import tkinter as tk
import json
import os
from tkinter import messagebox

cesta = r'C:\Users\Student\OneDrive - United States Army War College\Desktop\Project_1\Hokej\hraci.json'

# Funkce pro uložení hráče do JSON souboru
def ulozit_do_json(jmeno, prijmeni, rok_narozeni, cislo):
    novy_hrac = {
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "rok_narozeni": rok_narozeni,
        "cislo": cislo
    }

    # Pokud soubor existuje, načteme jeho obsah, jinak vytvoříme nový seznam
    if os.path.exists(cesta):
        with open(cesta, "r", encoding="utf-8") as soubor:
            hraci = json.load(soubor)
    else:
        hraci = []

    # Přidáme nového hráče
    hraci.append(novy_hrac)

    # Uložíme zpět do souboru
    with open(cesta, "w", encoding="utf-8") as soubor:
        json.dump(hraci, soubor, ensure_ascii=False, indent=4)

    messagebox.showinfo("Úspěch", f"Hráč {jmeno} {prijmeni} ({rok_narozeni}), číslo {cislo} byl přidán.")

# Funkce pro přidání čísla k již existujícím hráčům
def pridat_cisla_k_existujicim_hracum():
    if os.path.exists(cesta):
        with open(cesta, "r", encoding="utf-8") as soubor:
            hraci = json.load(soubor)

        # Umožníme uživateli přidat čísla k hráčům, kteří číslo ještě nemají
        for hrac in hraci:
            if "cislo" not in hrac:
                cislo = input(f"Zadejte číslo pro hráče {hrac['jmeno']} {hrac['prijmeni']}: ")
                hrac["cislo"] = cislo

        # Uložíme upravený seznam hráčů zpět do souboru
        with open(cesta, "w", encoding="utf-8") as soubor:
            json.dump(hraci, soubor, ensure_ascii=False, indent=4)

        messagebox.showinfo("Úspěch", "Čísla byla přidána k existujícím hráčům.")
    else:
        messagebox.showerror("Chyba", "Soubor 'hraci.json' neexistuje.")

# Funkce pro zobrazení hráčů ze souboru
def zobrazit_hrace():
    if os.path.exists(cesta):
        with open(cesta, "r", encoding="utf-8") as soubor:
            hraci = json.load(soubor)

        # Vytvoření okna pro zobrazení seznamu hráčů
        okno = tk.Tk()
        okno.title("Seznam hráčů")

        text = "\n".join([f"{hrac['jmeno']} {hrac['prijmeni']} ({hrac['rok_narozeni']}) - Číslo: {hrac['cislo']}" for hrac in hraci])
        label = tk.Label(okno, text=text, font=("Arial", 12), justify="left")
        label.pack(pady=10)

        okno.mainloop()
    else:
        messagebox.showerror("Chyba", "Soubor 'hraci.json' neexistuje.")

# Funkce pro rozdělení hráčů do týmů
def rozdelit_do_tymu():
    if os.path.exists(cesta):
        with open(cesta, "r", encoding="utf-8") as soubor:
            hraci = json.load(soubor)

        # Seřadíme hráče podle roku narození (od nejstaršího po nejmladší)
        hraci.sort(key=lambda x: x["rok_narozeni"])

        # Rozdělíme hráče rovnoměrně do týmů
        tym1 = []
        tym2 = []

        for i, hrac in enumerate(hraci):
            if i % 2 == 0:
                tym1.append(hrac)
            else:
                tym2.append(hrac)

        # Vytvoření okna pro zobrazení týmů
        okno = tk.Tk()
        okno.title("Rozdělení do týmů")

        # Vytvoříme text pro zobrazení týmů
        text_tym1 = "\n".join([f"{hrac['jmeno']} {hrac['prijmeni']} ({hrac['rok_narozeni']}) - Číslo: {hrac['cislo']}" for hrac in tym1])
        text_tym2 = "\n".join([f"{hrac['jmeno']} {hrac['prijmeni']} ({hrac['rok_narozeni']}) - Číslo: {hrac['cislo']}" for hrac in tym2])

        label_tym1 = tk.Label(okno, text="Tým 1:\n" + text_tym1, font=("Arial", 12), justify="left")
        label_tym1.pack(pady=10)

        label_tym2 = tk.Label(okno, text="Tým 2:\n" + text_tym2, font=("Arial", 12), justify="left")
        label_tym2.pack(pady=10)

        okno.mainloop()
    else:
        messagebox.showerror("Chyba", "Soubor 'hraci.json' neexistuje.")

# Funkce pro přidání nového hráče
def pridat_hrace(entry_jmeno, entry_prijmeni, entry_rok_narozeni, entry_cislo):
    jmeno = entry_jmeno.get().strip()
    prijmeni = entry_prijmeni.get().strip()
    rok_narozeni = entry_rok_narozeni.get().strip()
    cislo = entry_cislo.get().strip()

    if not jmeno or not prijmeni or not rok_narozeni or not cislo:
        messagebox.showwarning("Varování", "Všechna pole musí být vyplněná.")
        return

    try:
        rok_narozeni = int(rok_narozeni)
        cislo = int(cislo)
    except ValueError:
        messagebox.showerror("Chyba", "Rok narození a číslo hráče musí být čísla.")
        return

    # Uložíme hráče do JSON
    ulozit_do_json(jmeno, prijmeni, rok_narozeni, cislo)

    # Vyprázdníme vstupní pole
    entry_jmeno.delete(0, tk.END)
    entry_prijmeni.delete(0, tk.END)
    entry_rok_narozeni.delete(0, tk.END)
    entry_cislo.delete(0, tk.END)

# Hlavní okno
def hlavni_okno():
    window = tk.Tk()
    window.title("Zadání hráče a uložení do JSON")

    # Vstupy pro jméno, příjmení, rok narození a číslo
    label_jmeno = tk.Label(window, text="Jméno:", font=("Arial", 14))
    label_jmeno.pack(pady=5)
    entry_jmeno = tk.Entry(window, font=("Arial", 14), width=50)
    entry_jmeno.pack(pady=5)

    label_prijmeni = tk.Label(window, text="Příjmení:", font=("Arial", 14))
    label_prijmeni.pack(pady=5)
    entry_prijmeni = tk.Entry(window, font=("Arial", 14), width=50)
    entry_prijmeni.pack(pady=5)

    label_rok_narozeni = tk.Label(window, text="Rok narození:", font=("Arial", 14))
    label_rok_narozeni.pack(pady=5)
    entry_rok_narozeni = tk.Entry(window, font=("Arial", 14), width=50)
    entry_rok_narozeni.pack(pady=5)

    label_cislo = tk.Label(window, text="Číslo hráče:", font=("Arial", 14))
    label_cislo.pack(pady=5)
    entry_cislo = tk.Entry(window, font=("Arial", 14), width=50)
    entry_cislo.pack(pady=5)

    # Tlačítko pro přidání hráče
    button_pridat = tk.Button(window, text="Přidat hráče", font=("Arial", 14), command=lambda: pridat_hrace(entry_jmeno, entry_prijmeni, entry_rok_narozeni, entry_cislo))
    button_pridat.pack(pady=10)

    # Tlačítko pro zobrazení seznamu hráčů
    button_zobrazit = tk.Button(window, text="Zobrazit hráče", font=("Arial", 14), command=zobrazit_hrace)
    button_zobrazit.pack(pady=10)

    # Tlačítko pro rozdělení do týmů
    button_rozdelit = tk.Button(window, text="Rozdělit do týmů", font=("Arial", 14), command=rozdelit_do_tymu)
    button_rozdelit.pack(pady=10)

    # Tlačítko pro přidání čísel k existujícím hráčům
    button_pridat_cisla = tk.Button(window, text="Přidat čísla k existujícím hráčům", font=("Arial", 14), command=pridat_cisla_k_existujicim_hracum)
    button_pridat_cisla.pack(pady=10)

    window.mainloop()

# Spuštění hlavního okna
if __name__ == "__main__":
    hlavni_okno()
