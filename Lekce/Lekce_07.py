# Předpis funkce a parametry funkce
def scitej_dve_hodnoty(cislo_1, cislo_2):

    # VOLITELNÉ: dokumentace funkce
    """Vraci soucet dvou hodnot uvnitr parametru."""

    # VOLITELNÉ: vracené hodnoty
    return cislo_1 + cislo_2


# TAKHLE NE!
def vypocitej_sumu(cisla):
   suma = 0
  
   for cislo in cisla:
   suma = suma + cislo
   return suma

# TAKHLE ANO!
suma = sum(cisla)

# TAKHLE NE!
def email():
    pass

email()

# TAKHLE ANO!
def posli_email():
    pass

posli_email()

# TAKHLE NE!
def zobraz_nabidku(title, body, tlacitko, datum):
    pass

# TAKHLE ANO!
def vytvor_popisek(title, body):
    pass
def vytvor_tlacitko(tlacitko):
    pass
def vytvor_datum(datum):
    pass

# TAKHLE NE!
def posli_email_seznamu_klientu(klienti):
    """Filtruj pouze aktivni klienty a odesli zpravu"""
    for klient in klienti:
        if klient.je_aktivni:
            posli_email(klient)
            
            
# TAKHLE ANO!
def jen_aktivni_klienti(klienti):
    return [
        klient
        for klient in klienti
        if klient.je_aktivni
    ]

def posli_email(jen_aktivni):
    pass

def scitac_dvou_hodnot(cislo_1, cislo_2):
    """Vraci soucet dvou hodnot uvnitr parametru."""
    return cislo_1 + cislo_2

print(scitac_dvou_hodnot)

def scitac_dvou_hodnot(cislo_1, cislo_2):
    """Vraci soucet dvou hodnot uvnitr parametru."""
    return cislo_1 + cislo_2

print(scitac_dvou_hodnot(1, 2, 3))

def scitac_dvou_hodnot(cislo_1, cislo_2):
    """Vraci soucet dvou hodnot uvnitr parametru."""
    return cislo_1 + cislo_2

scitac_dvou_hodnot(1, 4)

# Původní definice funkce
def scitej_dve_hodnoty(cislo_1, cislo_2):
    """Vraci soucet dvou hodnot uvnitr parametru."""
    return cislo_1 + cislo_2


# Spuštění funkce
soucet_1 = scitej_dve_hodnoty(1, 14)
soucet_2 = scitej_dve_hodnoty(2, 8)

print(soucet_1, soucet_2, sep="\n")


#vice nasobne prirazeni
jmena = ("Matous", "Lukas")
prvni_jmeno = jmena[0]
druhe_jmeno = jmena[1]
print(prvni_jmeno, druhe_jmeno, sep=", ")

prvni_jmeno, druhe_jmeno = ("Matous", "Lukas")
print(prvni_jmeno, druhe_jmeno, sep=", ")

prvni_jmeno, druhe_jmeno = ("Matous", "Lukas", "Marek")
print(prvni_jmeno, druhe_jmeno, sep=", ")

#sbalovaci operator
jmena = ("Matous", "Marek", "Lukas", "Jan")
prvni_jmeno, druhe_jmeno, zbytek = jmena
print(prvni_jmeno, druhe_jmeno, sep=", ")

jmena = ("Matous", "Marek", "Lukas", "Jan")
prvni_jmeno, druhe_jmeno, *zbytek = jmena
print(prvni_jmeno, druhe_jmeno, sep=", ")
print(zbytek)

jmena = ("Matous", "Marek", "Lukas", "Jan")
prvni_jmeno, *zbytek, posledni_jmeno, = jmena
print(prvni_jmeno, posledni_jmeno, sep=", ")
print(zbytek)

jmena = ("Matous", "Marek", "Lukas", "Jan")
*zbytek, predposledni_jmeno, posledni_jmeno, = jmena
print(predposledni_jmeno, posledni_jmeno, sep=", ")
print(zbytek)

jmena = ("Matous", "Marek", "Lukas", "Jan")
*zbytek, *jine, posledni_jmeno, = jmena
print(posledni_jmeno)
print (zbytek, jine, sep="
")

jmena = ("Matous", "Marek", "Lukas", "Jan")
*zbytek, predposledni_jmeno, posledni_jmeno, = jmena
print(predposledni_jmeno, posledni_jmeno, sep=", ")
print(zbytek)

import os

var_1 = 1
var_2 = 1,

# různé datové typy
print(type(var_1), type(var_2), sep="
", end="

") 

# rozdělení jména a přípony souboru
jmeno, pripona = os.path.splitext("poznamky.txt") 
print(jmeno, pripona, sep="
", end="

")
*cele, = os.path.splitext("poznamky.txt")

# uchování jména i přípony v jednom objektu
print(cele)