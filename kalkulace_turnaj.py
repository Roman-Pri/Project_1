import tkinter as tk
from tkinter import messagebox

# Pevná proměnná
POCET_TRENERU_NA_ZAPAS = 2

# Funkce pro výpočty
def spocitat_naklady():
    try:
        # 1. Finanční parametry
        # Mandatorni_platby
        cena_za_led = float(entry_cena_led.get())
        cena_za_trener = float(entry_cena_trener.get())
        cena_za_rozhodci = float(entry_cena_rozhodci.get())
        cena_za_zdravotnik = float(entry_cena_zdravotnik.get())
        cena_za_vybaveni = float(entry_cena_vybaveni.get())

        # Běžné výdaje
        cena_za_oceneni = float(entry_cena_oceneni.get())
        cena_za_obcerstveni = float(entry_cena_obcerstveni.get())
        cena_za_cestovne = float(entry_cena_cestovne.get())

        # Investiční výdaje
        cena_za_marketing = float(entry_cena_marketing.get())
        cena_za_merch = float(entry_cena_merch.get())

        # 2. Početní parametry
        pocet_hracu = int(entry_pocet_hracu.get())
        pocet_brankaru = int(entry_pocet_brankaru.get())
        pocet_tyms_ve_skupine = int(entry_pocet_tyms_ve_skupine.get())
        pocet_skupin = int(entry_pocet_skupin.get())
        zapasy_na_tym_skupina = int(entry_zapasy_na_tym_skupina.get())
        zapasy_playoff = int(entry_zapasy_playoff.get())
        pocet_treneru_na_turnaj = int(entry_pocet_treneru.get())
        rozhodci_na_zapas = int(entry_pocet_rozhodci.get())
        pocet_organizatoru = int(entry_pocet_organizatoru.get())
        zdravotni_zabezpeceni = int(entry_pocet_zdravotni_zabezpeceni.get())

        # 3. Výpočty
        # Výpočet počtu zápasů na skupinu
        zapasy_na_skupinu = zapasy_na_tym_skupina * pocet_tyms_ve_skupine // 2

        # Výpočet celkového počtu zápasů na turnaj (pro všechny skupiny)
        celkovy_pocet_zapasu_na_turnaj = (zapasy_na_skupinu * pocet_skupin) + zapasy_playoff

        # Výpočet počtu hráčů a brankářů
        celkovy_pocet_hracu = pocet_hracu * pocet_tyms_ve_skupine * pocet_skupin
        celkovy_pocet_brankaru = pocet_brankaru * pocet_tyms_ve_skupine * pocet_skupin

        # Výpočty nákladů
        celkova_cena_led = cena_za_led * celkovy_pocet_zapasu_na_turnaj
        celkova_cena_treneri = cena_za_trener * celkovy_pocet_zapasu_na_turnaj
        celkova_cena_rozhodci = cena_za_rozhodci * celkovy_pocet_zapasu_na_turnaj * rozhodci_na_zapas
        celkova_cena_zdravotnik = cena_za_zdravotnik * celkovy_pocet_zapasu_na_turnaj
        cena_obcerstveni_zapas = cena_za_obcerstveni * (2 * pocet_hracu + 2 * pocet_brankaru + rozhodci_na_zapas + POCET_TRENERU_NA_ZAPAS + pocet_organizatoru + zdravotni_zabezpeceni)
        celkova_cena_obcerstveni = cena_obcerstveni_zapas * celkovy_pocet_zapasu_na_turnaj
        celkova_cena_vybaveni = cena_za_vybaveni * (celkovy_pocet_hracu + celkovy_pocet_brankaru)
        celkova_cena_oceneni = cena_za_oceneni
        celkova_cena_marketing = cena_za_marketing
        celkova_cena_merch = cena_za_merch
        celkova_cena_cestovne = cena_za_cestovne

        # Celkové náklady
        celkova_cena_za_turnaj = (celkova_cena_led + celkova_cena_treneri + celkova_cena_rozhodci + celkova_cena_zdravotnik + celkova_cena_oceneni + celkova_cena_obcerstveni +
                           celkova_cena_marketing + celkova_cena_merch + celkova_cena_vybaveni + celkova_cena_cestovne)

        # Výpočty poplatku na jednoho hráče
        minimalni_cena_za_jednoho_hrace = celkova_cena_za_turnaj / (celkovy_pocet_hracu + celkovy_pocet_brankaru)

        # Vytvoření seznamu marží (v procentech)
        marze = [20, 25, 30, 40, 50, 75, 100]

        # Výpočty ceny turnaje pro hrace s maržemi
        ceny_s_marzi = [round(minimalni_cena_za_jednoho_hrace * (1 + m / 100), 2) for m in marze]

        # Funkce pro výpočet výdělku
        def vypocet_vydelku(celkova_cena_za_turnaj):
            vysledky = []
            for m in marze:
                vydelek = (celkova_cena_za_turnaj * m) / 100
                vysledky.append((m, round(vydelek, 2)))  # Zaokrouhlení na dvě desetinná místa

            return vysledky

        vysledky = vypocet_vydelku(celkova_cena_za_turnaj)

        # Vytvoření nového okna pro zobrazení výsledků
        vysledek_okno = tk.Toplevel(root)
        vysledek_okno.title("Výsledky")

        # Vytvoření textového widgetu pro zobrazení výsledků
        text_widget = tk.Text(vysledek_okno, height=38, width=50, wrap=tk.WORD)
        text_widget.pack(padx=20, pady=20)

        # Seznam všech popisů pro ceny
        popisy = [
    "Cena za pronájem ledu:",
    "Cena za trenéry:",
    "Cena za rozhodčí:",
    "Cena za zdravotní zabezpečení:",
    "Cena za vybavení pro hráče:",
    "Cena nákladů na občerstvení:",
    "Cena za občerstvení na jeden zápas:",
    "Cena za cestovné:",
    "Cena za marketing:",
    "Cena za ceny:",
    "Cena za výrobu merchandise:",
    "Celková cena za celý turnaj:",
    "Celkový počet hráčů:",
    "Celkový počet brankářů:",
    "Celkový počet zápasů na skupinu:",
    "Celkový počet zápasů na turnaj:"
]

    # Přidání popisů pro marže
        popisy_marze = [
    "Cena na jednoho hráče s 20% marží:",
    "Cena na jednoho hráče s 25% marží:",
    "Cena na jednoho hráče s 30% marží:",
    "Cena na jednoho hráče s 40% marží:",
    "Cena na jednoho hráče s 50% marží:",
    "Cena na jednoho hráče s 75% marží:",
    "Cena na jednoho hráče s 100% marží:"
]
        # Seznam všech hodnot
        hodnoty = [
    celkova_cena_led,
    celkova_cena_treneri,
    celkova_cena_rozhodci,
    celkova_cena_zdravotnik,
    celkova_cena_vybaveni,
    celkova_cena_obcerstveni,
    cena_obcerstveni_zapas,
    celkova_cena_cestovne,
    celkova_cena_marketing,
    celkova_cena_oceneni,
    celkova_cena_merch,
    celkova_cena_za_turnaj,
    celkovy_pocet_hracu,
    celkovy_pocet_brankaru,
    zapasy_na_skupinu,
    celkovy_pocet_zapasu_na_turnaj
]
        # Maximální délka popisu pro zarovnání hodnot
        max_délka_popisu = max(len(popis) for popis in popisy)

        # Konfigurace pro zvýraznění
        text_widget.tag_configure("highlight", foreground="red")
        text_widget.tag_configure("highlight2", foreground="green")

        # Vytvoření textu s cenami a výsledky s dynamickým formátováním
        text_widget.config(state=tk.NORMAL)
        for i, (popis, hodnota) in enumerate(zip(popisy, hodnoty)):
            if popis == "Celková cena za celý turnaj:":
            # Zvýraznění celkové ceny za turnaj
                text_widget.insert(tk.END, f"{50*'-'}\n")
                text_widget.insert(tk.END, f"{popis.ljust(max_délka_popisu)} {str(hodnota).rjust(10)} Kč\n", "highlight")  # Zvýraznění
                text_widget.insert(tk.END, f"{50*'-'}\n")
            elif popis in ["Celkový počet hráčů:", "Celkový počet brankářů:", "Celkový počet zápasů na skupinu:", "Celkový počet zápasů na turnaj:"]:
                # Pro tyto řádky nebudeme přidávat "Kč"
                text_widget.insert(tk.END, f"{popis.ljust(max_délka_popisu)} {str(hodnota).rjust(10)}\n")
            else:
                # Zobrazení ceny s "Kč"
                text_widget.insert(tk.END, f"{popis.ljust(max_délka_popisu)} {str(hodnota).rjust(10)} Kč\n")

        text_widget.insert(tk.END, f"{50*'-'}\n")
        text_widget.insert(tk.END, f"Cena na jednoho hráče:{minimalni_cena_za_jednoho_hrace:24.0f} Kč\n", "highlight2")
        for popis, ceny in zip(popisy_marze, ceny_s_marzi):
            text_widget.insert(tk.END, f"{popis.ljust(max_délka_popisu)} {str(round(ceny)).rjust(10)} Kč\n", "highlight2")

        text_widget.insert(tk.END, f"{50*'-'}\n")

        for marze, vydelek in vysledky:
            text_widget.insert(tk.END, f"Výdělek s marží {marze:3}%: {vydelek:24.0f} Kč\n", "highlight2")

        # Nastavení textového widgetu na ne-editovatelné po vložení
        text_widget.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Chyba", f"Došlo k chybě: {str(e)}")

# 5. Vytvoření hlavního okna
root = tk.Tk()
root.title("Výpočet nákladů na hokejový turnaj")
root.config(bg="#f4f4f4")

# Rámce pro sloupce
frame_financni = tk.Frame(root, bg="#e6e6e6", bd=5, relief="solid")
frame_financni.grid(row=0, column=0, padx=20, pady=20, sticky="n", ipadx=10, ipady=10)

frame_pocetni = tk.Frame(root, bg="#e6e6e6", bd=5, relief="solid")
frame_pocetni.grid(row=0, column=1, padx=20, pady=20, sticky="n", ipadx=10, ipady=10)

# Finanční parametry
label_cena_led = tk.Label(frame_financni, text="Cena za pronájem 1 h ledu (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_led.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_cena_led = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_led.grid(row=0, column=1, padx=10, pady=5)

label_cena_trener = tk.Label(frame_financni, text="Cena za 1 x trenér / zápas (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_trener.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_cena_trener = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_trener.grid(row=1, column=1, padx=10, pady=5)

label_cena_rozhodci = tk.Label(frame_financni, text="Cena za 1 x rozhodčí / zápas (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_rozhodci.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_cena_rozhodci = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_rozhodci.grid(row=2, column=1, padx=10, pady=5)

label_cena_zdravotnik = tk.Label(frame_financni, text="Cena za zdravotní zabezpečení / zápas (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_zdravotnik.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_cena_zdravotnik = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_zdravotnik.grid(row=3, column=1, padx=10, pady=5)

label_cena_vybaveni = tk.Label(frame_financni, text="Cena za vybavení / hráč (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_vybaveni.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_cena_vybaveni = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_vybaveni.grid(row=4, column=1, padx=10, pady=5)

label_cena_oceneni = tk.Label(frame_financni, text="Náklady na ceny (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_oceneni.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_cena_oceneni = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_oceneni.grid(row=5, column=1, padx=10, pady=5)

label_cena_obcerstveni = tk.Label(frame_financni, text="Cena za občerstvení / osobu / zápas (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_obcerstveni.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_cena_obcerstveni = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_obcerstveni.grid(row=6, column=1, padx=10, pady=5)

label_cena_cestovne = tk.Label(frame_financni, text="Náklady na cestovné (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_cestovne.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_cena_cestovne = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_cestovne.grid(row=7, column=1, padx=10, pady=5)

label_cena_marketing = tk.Label(frame_financni, text="Náklady na marketing (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_marketing.grid(row=8, column=0, padx=10, pady=5, sticky="w")
entry_cena_marketing = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_marketing.grid(row=8, column=1, padx=10, pady=5)

label_cena_merch = tk.Label(frame_financni, text="Náklady na merchandise (Kč):", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_cena_merch.grid(row=9, column=0, padx=10, pady=5, sticky="w")
entry_cena_merch = tk.Entry(frame_financni, font=("Arial", 10))
entry_cena_merch.grid(row=9, column=1, padx=10, pady=5)

# Početní parametry (pro druhý sloupec)
label_pocet_hracu = tk.Label(frame_pocetni, text="Počet hráčů v týmu:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_pocet_hracu.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_pocet_hracu = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_pocet_hracu.grid(row=0, column=1, padx=10, pady=5)

label_pocet_brankaru = tk.Label(frame_pocetni, text="Počet brankářů v týmu:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_pocet_brankaru.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_pocet_brankaru = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_pocet_brankaru.grid(row=1, column=1, padx=10, pady=5)

label_pocet_tyms_ve_skupine = tk.Label(frame_pocetni, text="Počet týmů ve skupině:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_pocet_tyms_ve_skupine.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_pocet_tyms_ve_skupine = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_pocet_tyms_ve_skupine.grid(row=2, column=1, padx=10, pady=5)

label_pocet_skupin = tk.Label(frame_pocetni, text="Počet skupin:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_pocet_skupin.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_pocet_skupin = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_pocet_skupin.grid(row=3, column=1, padx=10, pady=5)

label_zapasy_na_tym_skupina = tk.Label(frame_pocetni, text="Počet zápasů na tým ve skupině:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_zapasy_na_tym_skupina.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_zapasy_na_tym_skupina = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_zapasy_na_tym_skupina.grid(row=4, column=1, padx=10, pady=5)

label_zapasy_playoff = tk.Label(frame_pocetni, text="Počet zápasů na tým v playoff:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_zapasy_playoff.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_zapasy_playoff = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_zapasy_playoff.grid(row=5, column=1, padx=10, pady=5)

label_pocet_treneru = tk.Label(frame_pocetni, text="Počet trenérů na turnaj:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_pocet_treneru.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_pocet_treneru = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_pocet_treneru.grid(row=6, column=1, padx=10, pady=5)

label_pocet_rozhodci = tk.Label(frame_pocetni, text="Počet rozhodčích na zápas:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_pocet_rozhodci.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_pocet_rozhodci = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_pocet_rozhodci.grid(row=7, column=1, padx=10, pady=5)

label_pocet_organizatoru = tk.Label(frame_pocetni, text="Počet organizátorů:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_pocet_organizatoru.grid(row=8, column=0, padx=10, pady=5, sticky="w")
entry_pocet_organizatoru = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_pocet_organizatoru.grid(row=8, column=1, padx=10, pady=5)

label_pocet_zdravotni_zabezpeceni = tk.Label(frame_pocetni, text="Počet zdravotníků:", anchor="w", bg="#e6e6e6", font=("Arial", 10))
label_pocet_zdravotni_zabezpeceni.grid(row=9, column=0, padx=10, pady=5, sticky="w")
entry_pocet_zdravotni_zabezpeceni = tk.Entry(frame_pocetni, font=("Arial", 10))
entry_pocet_zdravotni_zabezpeceni.grid(row=9, column=1, padx=10, pady=5)

# Tlačítko pro výpočet nákladů
button_vypocitat = tk.Button(root, text="Spočítat náklady", command=spocitat_naklady, bg="#4CAF50", fg="white", font=("Arial", 12))
button_vypocitat.grid(row=1, column=0, columnspan=2, pady=20)

# Spuštění aplikace
root.mainloop()