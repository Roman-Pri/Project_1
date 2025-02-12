# 1. Najdi hodnoty
#Nejprve ručně vytvoříš JSON soubor. 
# Potom vytvoř program, který načte zadaný json a získá z něj hodnoty ze specifických klíčů.
# program obsahuje:
# Vytvoř v editoru soubor udaje.json,
# zapiš do souboru udaje.json hodnoty uvedené výše,
# vytvoř nový skript main.py,
# v něm vytvoř funkci najdi_zadane_klice, která pracuje s parametrem jmeno_souboru,
# funkce najdi_zadane_klice musí nejprve otevřít zadaný soubor z parametru,
# funkce najdi_zadane_klice následně prohledá otevřený soubor.
# Pokud některý z procházených slovníků obsahuje klíč jmeno, hodnotu z toho klíče si uloží,
# nakonec vypiš jako výstup z funkce najdi_zadane_klic list, který obsahuje nalezené jména.


import json


# Následně pomocí funkce získej všechny klíče "jmeno"
def najdi_zadane_klice(jmeno_souboru: str) -> list:
    with open(jmeno_souboru) as json_soubor:
        obsah_jsonu = json.load(json_soubor)
    return [
            slovnik.get("jmeno") for slovnik in obsah_jsonu
    ]


if __name__ == "__main__":
    # Zavolej funkci a pomocí print() zobraz hodnoty
    print(najdi_zadane_klice("udaje.json"))
    

# 2. Seřaď klíče
# Vytvoř program, který:
# Nejprve seřadí klíče slovníku a uloží je jako JSON soubor,
# přečte seřazený obsah a zobrazí jej.
# Jednotlivé kroky, které program musí obsahovat:
# Zapiš proměnné uvedené výše,
# vytvoř funkci zapis_serazene_klice, která pracuje s parametry jmeno_souboru (použij proměnnou jmeno_souboru) a data (použij proměnnou data),
# funkce zapis_serazene_klice seřadí zadané klíče v data a zapíše JSON soubor,
# vytvoř funkci vypis_obsah_souboru, která pracuje s parametrem jmeno_souboru,
# funkce vypis_obsah_souboru přečte obsah právě vytvořeného seřazeného JSON souboru a vrátí jeho obsah,
# nakonec zapiš vrácenou hodnotu z funkce vypis_obsah_souboru do proměnné vysledek a vypiš ji.

import json


# Vytvoř funkci, která uloží seřazené klíče do JSON souboru
def zapis_serazene_klice(jmeno_souboru: str, data: dict) -> None:
    with open(jmeno_souboru, mode="w") as json_soubor:
        json.dump(data, json_soubor, sort_keys=True)


# Vytvoř funkci, která načte a vypíše obsah vytvořeného JSON souboru
def vypis_obsah_souboru(jmeno_souboru):
    with open(jmeno_souboru) as json_soubor:
        return json.load(json_soubor)


# Definuj proměnné 'jmeno_souboru' a 'data'
jmeno_souboru = "serazene.json"
data = {'4': 5, '6': 7, '1': 3, '2': 4}

# Zavolej obě funkce
zapis_serazene_klice(jmeno_souboru, data)
vysledek = vypis_obsah_souboru(jmeno_souboru)
print(vysledek)

#3. Zapiš a přečti CSV
# Vytvoř program, který vytvoří csv soubor ze zadaných hodnot a následně tento soubor otevře 
# a vypíše každý řádek z csv souboru.
# Jednotlivé kroky, které program musí obsahovat:
# Zapiš proměnnou uvedenou výše,
# zapiš tyto hodnoty do CSV souboru, 
# pojmenuj jej jako nove.csv,
# následně nově vytvořený soubor otevři, 
# načti jeho obsah, zapiš tento obsah do proměnné csv_data a vypiš jej podle ukázky níže.

import csv

# Vytvoř proměnnou 'data'
data = [
    [10, "a1", 1],
    [12, "a2", 3],
    [14, "a3", 5],
    [16, "a4", 7],
    [18, "a5", 9]
]


# Zapiš soubor typu CSV se jménem 'nove.csv'
with open("nove.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Přečti nově zapsaný CSV soubor
with open("nove.csv", newline="") as csvfile:
    csv_data = csv.reader(csvfile, delimiter=" ")

    for row in csv_data:
        print(", ".join(row))
        
        




    