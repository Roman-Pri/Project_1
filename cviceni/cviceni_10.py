# 1. Čtečka řádků
# Tvým úkolem bude vytvořit funkci, která umí:
# Načíst soubor,
# ošetří případ, kdy soubor není nalezen.

# Pro tuto úlohu budeš potřebovat vytvořit textový soubor jazyky.txt. Tento soubor bude obsahovat text:
# Python,
# Scala,
# JavaScript,
# Java.

# Tvůj program musí obsahovat:
# Definici uživatelské funkce nacti_radky,
# funkce nacti_radky pracuje pouze s jedním parametrem cesta_k_souboru,
# pokud soubor existuje, přečti jeho obsah a ulož jej do proměnné vysledek,
# pokud soubor neexistuje a nastane výjimka, situaci ošetři a vypiš ohlášení "Soubor:  neexistuje!",
# nakonec vrácenou hodnotu v proměnné vysledek vypiš.

def nacti_radky(cesta_k_souboru: str):
    try:
        soubor = open(cesta_k_souboru)

    except FileNotFoundError:
        print(f'Soubor: {cesta_k_souboru} neexistuje!')
        obsah = []
    else:
        obsah = soubor.read()
        soubor.close()
    finally:
        return obsah


vysledek = nacti_radky("jazyky.txt")
print(vysledek)


# 2. Sčítáme špinavý list
# Nyní bude tvým úkolem vytvořit funkci secti_hodnoty, 
# která bude umět sečíst všechna čísla, která najde v zadaném listu. 
# Jak v číselné, tak v textové podobě.

# Skript by si měl poradit i v takovém případě, kdy v listu nebudou jen čísla. 
# Bude se snažit přetypovat hodnotu na float a pokud neuspěje, na hodnotu upozorní.
# Správný postup musí obsahovat následující:
# Zapiš proměnnou uvedenou výše,
# vytvoř funkci secti_hodnoty, která bude mít pouze parametr udaje,
# funkce se snaží každou hodnoty zapsat jako float,
# pokud nenastane výjimka, hodnotu přičte,
# pokud nastane výjimka, odchytne ji, upozorní na hodnotu a pokračuje,
# nakonec funkce secti_hodnoty vrátí výsledek,výslednou hodnotu vypiš podle vzoru níže.

def secti_hodnoty(udaje):
    vysledek = 0.0

    for hodnota in udaje:
        try:
            cislo = float(hodnota)

        except Exception:
            print(f"Hodnota {hodnota} není číselný údaj.")
        else:
            vysledek += float(cislo)

    return vysledek


test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, [], '\\n', 4]
print("Výsledek:", secti_hodnoty(test))


# 3. Slovníkový vyhledávač
# V tomto úkolu budeš opět vytvářet funkci, tentokrát s názvem obsahuje_klic_a_hodnotu.
# Tato funkce bude ve slovníku vyhledávat zadanou hodnotu u zadaného klíče.


# Zapiš proměnnou uvedenou výše,
# definovat funkci obsahuje_klic_a_hodnotu,
# funkce obsahuje_klic_a_hodnotu bude pracovat se 3 parametry: klic, hodnota a slovnik (dodržuj pořadí),
# zkoušet, jestli dohledá hodnotu v klic ve slovnik,
# pokud dostane výjimku KeyError, vrátí False,
# pokud nedostane výjimku KeyError, 
# vyzkouší jestli odpovídá zadaný parametr klic hodnotě v parametru hodnota,
# pokud odpovídá nalezená hodnota, hodnotě zadané, vrať True,
# pokud neodpovídá nalezená hodnota, hodnotě zadané, vrať False,vypsat výstup pomocí funkce print() podle ukázky.


muj_slovnik = {
    'jmeno':'Pepa',
    'prijmeni': 'Novak',
    'rok_narozeni': 1990
}

def obsahuje_klic_a_hodnotu(klic: str, hodnota: str, slovnik: dict) -> bool:
    try:
        nalezena_hodnota = slovnik[klic]

    except KeyError:
        print(f'Klíč: {klic}, nenalezen.')
        vysledek = False
    else:
        print(f"Klíč: {klic}, nalezen.")

        if nalezena_hodnota == hodnota:
            vysledek = True
        else:
            print(f"Hodnota: {hodnota}, nenalezena.")
            vysledek = False
    finally:
        return vysledek


print(obsahuje_klic_a_hodnotu("jmeno", "Pepa", muj_slovnik))