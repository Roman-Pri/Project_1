# 1. vynasob cisla
# V této úloze napíšeš uživatelskou funkci, která vezme dvě číselné hodnoty a vrátí jejich součin.
# Program musi obsahovat:
# zapiš proměnné uvedené výš,
# vytvoř funkci vynasob, která bude mít 2 parametry num1 a num2,
# vytvoř proměnnou vysledek, do které ulož výstup funkce,
# vypiš hodnotu proměnné vysledek.

# Vytvor promenne a uloz do ne hodnoty dle zadani
prvni_cislo = 5
druhe_cislo = 5

# Vytvor funkci, ktera vezme na vstupu dve cisla a vynasobi je
def vynasob(num1, num2):
    return num1 * num2

# Uloz vystup z funkce do promenne vysledek
vysledek = vynasob(prvni_cislo, druhe_cislo)

# Vytiskni vysledek
print(f'Vysledek je: {vysledek}')

#2. Zdvojnásob znaky
# Vytvoř uživatelskou funkci, která zdvojnásobí všechny znaky zadaného stringu.
# Program musí obsahovat tyto kroky:
# zapiš proměnné uvedené nize,
# vytvoř funkci zdvojnasob_vsechny_znaky, která bude mít jeden parametr zadani,
# vytvoř proměnnou vysledek , do které ulož výstup funkce,
# vypiš hodnotu proměnné vysledek.

# Vytvor promennou a uloz zadanou hodnotu
vstup = "Ahoj všem"

# Vytvor funkci ktera vezme string na vstupu
def zdvojnasob_vsechny_znaky(zadani: str) -> str:
    zdvojene = []

    for znak in zadani:
        zdvojene.append(znak * 2)
    return "".join(zdvojene)

# Uloz vystup funkce do promenne vysledek
vysledek = zdvojnasob_vsechny_znaky(vstup)

# Vytiskni vysledek
print(vysledek)


# 3. Můj operační systém
# Zapiš uživ. funkci, která ověří zda operační systém na tvém pc je Windows či nikoliv.
# Tvůj zápis musí obsahovat:
# Definici a spuštění uživ. funkce je_os_windows,
# pomocnou knihovny sys s příslušnou metodou na ověření operačního systému,
# uživ. funkce je_os_windows, která vrátí hodnotu True, pokud pracuješ na op. systému windows. Jinak vrátí hodnotu False.

import sys


def je_os_windows():
    """
    Vrať bool hodnotu True, pokud je můj os win. Jinak  vrať False.
    """
    return sys.platform.startswith("win")


print(je_os_windows())


# 4. Největší společný dělitel
# NSD (GCD v angličtině) je zkratka pro největší společný dělitel (greatest common divisor).
# Tvým úkolem je vytvořit funkci najdi_gcd, která spočítá největší společný dělitel dvou celých čísel (int).
# Zadaná čísla jsou 12 a 16.
# Pomůcka, jak spočítat největší společný dělitel:
# hledáš největší společný dělitel pro čísla 12 a 16,
# nejprve použiješ modulo, abys zjistil zbytek 12 % 16, tedy 12,
# nyní vezmeš jako první číslo 16, tedy 16 % 12, kdy 12 představuje zbytek po prvním dělení. 
# Zbytek po dělení 4,třetí krok se v podstatě opakuje, 
# vezmu předchozí druhou hodnotu a zbytek po dělení, tedy 12 % 4, 
# nyní je však zbytek 0, takže hledání je u konce,největší společný dělitel pro čísla 12 a 16 je 4.

# program musi obsahovat:
# Zapiš proměnné uvedené výš,
# vytvoř uživatelskou funkci najdi_gcd s parametry x1, x2,
# najdi největšího společného dělitele a ulož jej do proměnné vysledek,
# vypiš obsah proměnné vysledek.

# Vytvoř proměnné a ulož do nich zadaná čísla
prvni_cislo = 12
druhe_cislo = 16

def najdi_gcd(x1: int, x2: int) -> int:
    """
    Vrať celočíselnou hodnotu představující největší společný dělitel pro
    parametry "x1" a "x2".
    """
    while x2 > 1:
        zbytek_po_deleni = x1 % x2

        if not zbytek_po_deleni:
            break

        x1, x2 = x2, zbytek_po_deleni
    return x2

# Najdi největšího společného dělitele a ulož jej do proměnné
vysledek = najdi_gcd(prvni_cislo, druhe_cislo)

# Tisk výsledku
print(vysledek)