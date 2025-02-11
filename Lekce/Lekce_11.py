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