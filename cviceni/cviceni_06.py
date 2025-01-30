# prvni priklad Kámen, nůžky, papír
# Pro tuto úlohu budeš potřebovat nahrát knihovnu random. Tvým úkolem bude napsat hru kámen, nůžky, papír.
# 1] Naimportuj modul random,
# 2] vytvoř list moznosti s hodnotami 'kamen', 'nuzky', 'papir',
# 3] vytvoř proměnnou hrac a ulož do ní hodnotu "kamen",
# 4] vytvoř proměnnou pocitac, které bude náhodně přiřazen prvek z listu moznostipokud hráč vyhraje, vypiš "Vyhrál jsi!", pokud prohraje, vypíš "Prohrál jsi:(", v případě remízy vytiskni "Nerozhodně".

# Naimportuj modul random
import random

# Vytvorte list moznosti
moznosti = ['kamen', 'nuzky', 'papir']

# Vytvorte promennou hrac a ulozte do ni hodnotu kamen
hrac = "kamen"

# Vytvorte promennou pocitac
pocitac = random.choice(moznosti)

# Vytisknete volbu cloveka a pocitace
print("Hráč:", hrac)
print("Počítač:", pocitac)
# Podminky zahrnujici ruzne kombinace voleb hrace a pocitace a tisk vysledku
if hrac == 'kamen' and pocitac == 'nuzky':
    print("Vyhrál jsi!")

elif hrac == 'kamen' and pocitac == 'papir':
    print("Prohrál jsi!")

else:
    print("Nerozhodně")



# 2.priklad Vytvoř složky
#Pomocí modulu os napiš takový kód, který v aktuálním umístění vytvoří tyto tři prázdné adresáře:
# obrazky,
# texty,
# gify.
# Program musi:
# 1 Nahrát knihovnu os,
# 2 vytvořit proměnnou jmena_slozek, kam vložíš stringy "obrazky", "texty", "gify",
# 3 projít jednu hodnotu za druhou z proměnné jmena_slozek,
# 4 ověřit, jestli daný string neexistuje a není adresářem,
# 5 pokud existuje, vypsat oznámení "Složka již existuje!"
# 6 pokud neexistuje, vytvořit složku a vypsat oznámení "Tvořím novou složku: ".
# 7 závěrem vypsat: "Všechny složky existují".
import os

jmena_slozek = ("obrazky", "texty", "gify")

for slozka in jmena_slozek:
    if os.path.exists(slozka) and os.path.isdir(slozka):    #Funkce os.path.exists je součástí modulu os v Pythonu. Používá se k ověření, zda existuje cesta (soubor nebo adresář) v systému.
        print("slozka existuje!")                           #Funkce os.path.isdir se používá k ověření, zda zadaná cesta ukazuje na existující adresář (složku).
    else:
        print(f"Tvorim novou slozku: {slozka}")
        os.mkdir(slozka)                                    #Funkce os.mkdir slouží k vytvoření nového adresáře (složky) v systému. Pokud adresář již existuje, vyvolá chybu.
print("Vsechny slozky existuji!")


#3.priklad - kostka
# Pro tuto úlohu budeš potřebovat nahrát knihovnu random. Tvým úkolem bude simulovat hod kostkou.
# Program musí obsahovat:
# 1] Naimportuj knihovnu random,
# 2] vytvoř proměnnou min_hodnota a ulož do ní integer 1,
# 3] vytvoř proměnnou max_hodnota a ulož do ní integer 6,
# 4] vytvoř řízenou nekonečnou smyčku,
# 5] nejprve vypiš: "Házím kostkou..",
# 6] vytvoř proměnnou kostka_hodnota, které bude náhodně přiřazeno integer od min_hodnota do max_hodnota,
# 7] následně doplň oznámení: "Na kostce je: ",
# 8] pokud kostka_hodnota bude obsahovat hodnotu 6, hod se provede znovu,
# 9] pokud padne jiné číslo, než 6 program se ukončí.
import random

min_hodnota = 1
max_hodnota = 6


while True:
    print("Hazim kostkou!")
    kostka_hodnota = random.randint(min_hodnota,max_hodnota)  #Funkce random.randint slouží k vygenerování náhodného celého čísla z uzavřeného intervalu (včetně dolní i horní hranice).
    if kostka_hodnota == 6:
        print(f"Na kostce je hodnota {kostka_hodnota}. Hazim znovu!")
        continue
    else:
       print(f"Na kostce je hodnota: {kostka_hodnota}")
       break