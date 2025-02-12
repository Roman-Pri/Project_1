import sys

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

print(type(chuckuv_slovnik))

# bez knihovny nemůžeš pracovat s JSON objekty
import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# metoda 'dumps' uloží objekt do stringu
vystup_s_jsonem = json.dumps(chuckuv_slovnik)

print(vystup_s_jsonem)

# overeni dat typu
chuckuv_slovnik = {
 "jmeno": "Chuck Norris",
 "neuspech": None,
 "kliky": "vsechny",
 "konkurence": False,
 "fanousek": "Łukasz"
}

vystup_s_jsonem = json.dumps(chuckuv_slovnik)

# Doplněný výstup u funkci "type"
print(type(vystup_s_jsonem))

#zapis do souboru

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# funkci 'open' nachystáš objekt v Pythonu
json_soubor = open("prvni_json_soubor.json", mode="w")

# metoda 'dump' uloží objektu do souboru
json.dump(chuckuv_slovnik, json_soubor)

# ... nezapomeň objekt ukončit
json_soubor.close()

# ulozeni pomoci kontextoveho manazera

with open("prvni_json_soubor.json", mode="w") as json_soubor:
   # metoda "dump" uloží objektu do souboru
   json.dump(chuckuv_slovnik, json_soubor)
   
# funkce loads - nacteni json (str) do slovniku
# metoda 'loads' přemapuje objekt ze stringu zpět na slovník
vystup_slovnik = json.loads(vystup_s_jsonem)
print(vystup_slovnik)
# kontrola dat.typu - slovnik
print(type(vystup_s_jsonem))

# funkce load
#with open("druhy_json_soubor.json", mode="r") as json_soubor:
   # .. uložím obsah souboru
   #obsah_jsonu = json.load(json_soubor)

#print(obsah_jsonu)


#argument ASCII
chuckuv_slovnik = {
 "fanousek": "Łukasz"
}

# argument "ensure_ascii" součástí metody "dumps"
vystup_s_jsonem = json.dumps(chuckuv_slovnik, ensure_ascii=False)
print(vystup_s_jsonem)

# odsazeni json
chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# argument 'indent' součástí metody 'dumps'
# .. použité 4 mezery, ale hodnotu můžeš upravit
vystup_s_jsonem = json.dumps(chuckuv_slovnik, indent=20)
print(vystup_s_jsonem)


# serazeni klicu
chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# argument 'sort_keys' součástí metody 'dumps'
vystup_s_jsonem = json.dumps(chuckuv_slovnik, sort_keys=True)
print(vystup_s_jsonem)



# CSV
# Nezapomeň nahrát knihovnu, jinak soubor nevytvoříš
import csv

hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

# ... nachystáš nový soubor pro zápis
nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")

# ... vytvoříš zapisovací objekt, který do souboru zapíše údaje
zapisovac = csv.writer(nove_csv)

# ... nejprve zapíšeš záhlaví
zapisovac.writerow(hlavicka)

# ... potom první údaj
zapisovac.writerow(osoba_1)

# ... druhý údaj
zapisovac.writerow(osoba_2)

# ... nakonec objekt a soubor uzavřeš
nove_csv.close()


# zapis writerows

hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")

zapisovac = csv.writer(nove_csv)
zapisovac.writerows(
   ( 
       hlavicka,
       osoba_1,
       osoba_2
   )
)
nove_csv.close()


# zapis writerows s kontextovym manazerem

hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

with open("prvni_tabulkovy_soubor.csv", mode="w") as nove_csv:
   zapisovac = csv.writer(nove_csv)
   zapisovac.writerows(
      (
          hlavicka,
          osoba_1,
          osoba_2
      )
  )
   
   
# zapis pomoci Dictwriter - mas uz zahlavi

osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

# ... nachystáš nový soubor pro zápis
nove_csv = open("druhy_tabulkovy_soubor.csv", mode="w")

# ... z existujících klíčů si vytvoříš záhlaví
zahlavi = osoba_1.keys()

# ... nachystáš si nový zapisovač, kterému nastavíš parametr "fieldnames"
zapisovac = csv.DictWriter(nove_csv, fieldnames=zahlavi)

# ... nejprve zapíšeš záhlaví
zapisovac.writeheader()

# ... následně oba údaje
zapisovac.writerow(osoba_1)
zapisovac.writerow(osoba_2)

# ... nakonec soubor ukončíš
nove_csv.close()


# zapic DictWriter pomoci kontextoveho manazeru
osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

with open("druhy_tabulkovy_soubor.csv", mode="w") as nove_csv:
    zahlavi = osoba_1.keys()
    zapisovac = csv.DictWriter(nove_csv, fieldnames=zahlavi)

    zapisovac.writeheader()
    zapisovac.writerow(osoba_1)
    zapisovac.writerow(osoba_2)
    
# cteni pomoci reader
# Načteš soubor "csv" jako objekt "cteni_csv"
cteni_csv = open("prvni_tabulkovy_soubor.csv")

# Vytvoříš iterovatelný objekt se všemi záznamy ze souboru
cteni = csv.reader(cteni_csv)

# Vypíšeš obsah "csv" souboru s pomocí funkce "tuple"
print(tuple(cteni))

# Ukončíš soubor
cteni_csv.close()


# Reader  v kontextovem manazeru
with open('prvni_tabulkovy_soubor.csv') as cteni_csv:
    cteni = csv.reader(cteni_csv)
    print(tuple(cteni))
    

# cteni souboru pomoci DictReader
# Načteš soubor "csv" jako objekt "cteni_csv"
cteni_csv = open("prvni_tabulkovy_soubor.csv")

# Vytvoříš iterovatelný objekt se všemi záznamy ze souboru
cteni = csv.DictReader(cteni_csv)

# Vypíšeš obsah "csv" souboru s pomocí funkce "tuple"
print(tuple(cteni))

# Ukončíš soubor
cteni_csv.close()




# ukazka Dict Reader v kontextovem manazeru
with open('druhy_tabulkovy_soubor.csv') as cteni_csv:
    cteni = csv.DictReader(cteni_csv)
    print(tuple(cteni))
    
    
    
    
# Argument - oddelovac
osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

with open("druhy_tabulkovy_soubor.csv", mode="w") as nove_csv:
    zahlavi = osoba_1.keys()
    # přidaný parametr 'delimiter' s nastaveným středníkem
    zapisovac = csv.DictWriter(nove_csv, delimiter=";", fieldnames=zahlavi)
    zapisovac.writeheader()
    zapisovac.writerow(osoba_1)
    zapisovac.writerow(osoba_2)
    
    
# Argument - vyber dialekt
osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

with open("druhy_tabulkovy_soubor.csv", mode="w") as nove_csv:
    zahlavi = osoba_1.keys()
    # přidaný parametr 'dialect' s nastaveným formátem 'excel-tab'
    zapisovac = csv.DictWriter(nove_csv, dialect="excel-tab", fieldnames=zahlavi)
    zapisovac.writeheader()
    zapisovac.writerow(osoba_1)
    zapisovac.writerow(osoba_2)
    
    
# Systemove argumenty - sys, prozrazeni oper. systemu

if sys.platform == "darwin":
    print("Jsem na Macu..")
elif sys.platform == "windows":
    print("Jsem na Windowsech..")
elif sys.platform == "linux":
    print("Jsem na Linuxu..")
    
    
# Systemove argumenty - ukonceni programu
jmeno = "Petr"
prijmeni = "Svetr"
if not jmeno or not prijmeni:
 print("Chybí jméno nebo příjmení")
 # jednička představuje obecně jakoukoliv chybu
 sys.exit(1)
else:
 print("Program pokračuje..")
 
 