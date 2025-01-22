
# ukazka vstupu
def spoj_cele_jmeno(jmeno, prijmeni):  #parametry - jmeno, prijmeni
    """
    Spoj zformatovane hodnoty v parametrech.

    Priklad:
    >>> formatuj_cele_jmeno("Petr", "Svetr")
    p.svetr
    """
    return ".".join(
        (
            jmeno[0].lower(),
            prijmeni.lower()
        )
    )

print(spoj_cele_jmeno("Adam", "Novak"))     #argumenty - Adam, Novak


#Pozicni a klicove parametry
def uloz_informace(jmeno, prijmeni, telefon):
    return {
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "telefon": telefon
}

print(uloz_informace("Petr", "Svetr", "+420 777 666 555"))

# klicove parametry
def vypocitej_hodnotu(koef_1, koef_2, koef_3):
    """
    Vypocitej hodnotu na zaklade tri zadanych koeficinetu.
    """
    return (1/koef_1) * (koef_2 ** koef_3)

print(vypocitej_hodnotu(1, 2, 4))

print(vypocitej_hodnotu(koef_1=0.5, koef_2=3, koef_3=2)) #zapis pomoci klicovych parametru, dokonce nemusi byt zapis ve stanovenem poradi

# default parametry
def vytvor_pozdrav(jmeno="Matous"):
    print("Ahoj,", jmeno)

vytvor_pozdrav() #default
vytvor_pozdrav("Lukas") #prepsani defaultu

# Position - only parametry
def napis_pozdrav(jmeno, /, registrovany):
    if not registrovany:
        print("Nejsi uzivatel!")
    print("Ahoj,", jmeno)


napis_pozdrav("Matous", True)

# *args
def vypocitej_prumer(args): #bez pouziti hvezdicky
    return sum(args) / len(args)


moje_cisla = [1, 2, 3, 4, 5]
print(vypocitej_prumer(moje_cisla))

def vypocitej_prumer(*args): #Nyní v podstatě funkci vypocitej_prumer zapsanou hvězdičkou oznamuješ, že parametr args může mít jakýkoliv počet hodnot.
    return sum(args) / len(args)

print(vypocitej_prumer(1, 2, 3, 4, 5)) 

# **kwargs
def vytvor_slovnik(**kwargs):
    vysledek = dict()

    for klic, hodnota in kwargs.items():
        vysledek[klic] = hodnota
    return vysledek


print(vytvor_slovnik(jmeno="Matous", prijmeni="Holinka"))

# uzavreny ramec
def vnejsi_funkce():
    # tento rámec byl doposud *lokální*
    # pokud se uvnitř lokálního rámce nachází jiný *lokální rámec*,
    # .. jde současně o *uzavírající rámec* 
    print("Ted se nachazis ve vnejsi funkci")

    def vnitrni_funkce():
        # oddělený *lokální rámec*
        print("Ted se nachazis ve vnitrni funkci")
    
    vnitrni_funkce()
vnejsi_funkce()


# Dokumentace f-ce
def vypocitej_vyskyt_dat(text):
    """
    Vrátí slovník, který obsahuje vypočítaný výskyt hodnot
    v parametru "text".

    Parametry:
    :text: list nebo tuple
        Zadaný objekt, jehož hodnoty funkce počítá.

    :vyskyt: dict
        Eviduje výskyty jednotlivých hodnot. 
    """
    vyskyt = {}
    
    for slovo in text:
        vyskyt[slovo] = vyskyt.setdefault(slovo, 0) + 1

    return vyskyt


print(vypocitej_vyskyt_dat(("a", "b", "a", "c", "d", "b", "a")))

# dokumentace s prikladem
def vypocitej_vyskyt_dat(text):
    """
    Vrátí slovník, který obsahuje vypočítaný výskyt hodnot
    v parametru "text".

    Příklad:
    >>> vysledek = vypocitej_vyskyt_dat("a", "b", "a")
    >>> vysledek
    {"a": 2, "b": 1}
    """
    vyskyt = dict()

    for slovo in text:
        vyskyt[slovo] = vyskyt.setdefault(slovo, 0) + 1

    return vyskyt


print(vypocitej_vyskyt_dat(("a", "b", "a", "c", "d", "b", "a")))