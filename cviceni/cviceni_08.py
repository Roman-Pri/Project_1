# 1. Anagram
# V této úloze si vyzkoušíš identifikaci anagramů.
# Anagramy jsou dvě a více slov složených ze stejných znaků. Třeba anglická slova ship a hips.
# Pokud budeš chtít, můžeš se mrknout na tento web, který generuje anagramy. https://wordsmith.org/anagram/
# Tvoje úloha musí obsahovat tyto kroky:
# Vytvoř funkci je_anagram, která může mít jako vstup libovolně dlouhý tuple,
# z první hodnoty v sekvenci stanoví vzor, jehož písmena seřadí,
# funkce potom projde všechny hodnoty ze vstupu a ověří, jestli nejsou anagram,
# pokud JSOU anagram, vrátí True,
# pokud NEJSOU anagram, vrátí False,
# vyzkoušej funkci spustit podle zadání v ukázce.

def je_anagram(*args) -> bool:
    """
    Vrati boolean True, pokud jsou vsechny parametry anagramy.
    Jinak vrati False.

    Priklad:
    >>> print(je_anagram("ship", "hips", "hisp"))
    True
    >>> print(je_anagram_matous("ship", "hips", "duck"))
    False
    """
    vzor = sorted(args[0])

    for slovo in args:
        if sorted(slovo) != vzor:
            return False
    else:
        return True


print(
    je_anagram("ship", "hips", "hisp"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)


# 2. Filtruj emaily
# Vytvoř program, který ze zadaného listu vytáhne emaily, které obsahují čísla.
# Tvoje úloha musí obsahovat tyto kroky:
# Zapiš hodnoty uvedené niz,
# vytvoř funkci filtruj_adresy_s_cisly, 
# funkce bude mít jeden parameter, 
# posbírá ze zadaného setu pouze emaily, které obsahují čísla,
# výstup z funkce ulož do proměnné vysledek,
# vypiš obsah proměnné vysledek.

# Vytvor list se zadanymi hodnotami
adresy = [
    "matous@holinka.com",
    "danek11@seznam.cz",
    "rennud15@gmail.com",
    "pepa@centrum.cz"
]

def filtruj_adresy_s_cisly(emaily: list) -> list:
    """
    Ze zadaneho objektu emailu vyber pouze ty, ktere obsahuji ciselne znaky.

    Priklad:
    >>> print(filtruj_adresy_s_cisly(["matous@holinka.com", "danek11@seznam.cz"]))
    ["danek11@seznam.cz"]
    """
    ciselne_hodnoty = []

    for email in emaily:
        for znak in email:
            if not znak.isnumeric():
                continue
            ciselne_hodnoty.append(email)
            break

    return ciselne_hodnoty

# Uloz vystup funkce do promenne
vysledek = filtruj_adresy_s_cisly(adresy)

# Vytiskni obsah promenne vysledek
print(vysledek)



# 3. Prvočíslo
# Tentokrát bude tvým úkolem napsat dvě funkce:
# je_prvocislo, která posoudí, jestli je zadané číslo prvočísl o, nebo není,
# generuj_interval_prvocisel, která vytvoří interval prvočísel až po zadanou hodnotu.

# Prvočísla jsou taková čísla, která jsou dělitelná pouze jedničkou nebo sama sebou.
# Tvoje úloha musí obsahovat tyto kroky:
# Vytvoř funkci je_prvocislo, s parametrem cislo, který vezme samotné číslo a jako druhý parametr prvocisla,
# vytvoř funkci generuj_interval_prvocisel, která nejprve vytvoří interval všech čísel od nuly až po parametr stop (včetně této hodnoty),prochází interval a všechny jeho hodnoty. 
# Pokud narazí na 0 nebo 1, přeskoč je,
# vytvoř zanořený cyklus, který prochází hodnoty v rozsahu range(2, cislo),
# pokud platí, že hodnota z vnějšího cyklu cislo je dělitelná beze zbytku hodnotou z vnitřního cyklu filtr_cislo, 
# přeruš vnitřní cyklus. Nakonec ulož hodnotu v filtr_cislo do proměnné vysledek,
# získané údaje vrať jako tuple,vyzkoušej tvoji úlohu na těchto voláních:

def je_prvocislo(cislo: int, prvocisla: tuple) -> bool:
    """
    Vrat boolean hodnotu True, pokud je zadane cislo     prvocislo.

    Jinak vrat False.

    Priklad:
    >>> print(je_prvocislo(23, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
    True

    >>> print(je_prvocislo(10, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
    False
    """
    return cislo in prvocisla


def generuj_interval_prvocisel(stop: int) -> tuple:
    """
    Vrat interval hodnot od start do stop.

    Priklad:
    >>> print(generuj_interval_prvocisel(10))
    (2, 3, 5, 7)

    >>> print(generuj_interval_prvocisel(20))
    (2, 3, 5, 7, 11, 13, 17, 19)
    """
    vsechna_cisla = tuple(range(stop + 1))
    vysledek = list()

    for cislo in vsechna_cisla:
        if cislo == 0 or cislo == 1:
           continue
       
           for filtr_cislo in range(2, cislo):
            if cislo % filtr_cislo == 0:
                break
        else:
            vysledek.append(cislo)

    return tuple(vysledek)


print(
    je_prvocislo(23, generuj_interval_prvocisel(30)),
    je_prvocislo(233, generuj_interval_prvocisel(300)),
    je_prvocislo(146, generuj_interval_prvocisel(300)),
    sep="\n"
)


# 4. Sběr emailů
# Vytvoř program, který ze zadaného textu vytáhne emaily.
# Tvoje úloha musí obsahovat tyto kroky:
# zapiš hodnoty uvedené niz,
# vytvoř funkci uloz_emailove_adresy, 
# funkce bude mít jeden parameter text, vezme zadaný text a vytáhne z něj všechny emailové adresy,
# výstup z funkce, vrať do proměnné vysledek,vypiš obsah proměnné vysledek podle ukázky níž.

# Vytvor promennou text a uloz do ni zadany text
text = '''\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc 
tristique fringilla congue. Donec ante diam cnn@info.com, dapibus lacinia vulputate vitae, ullamcorper in justo. Maecenas massa purus, ultricies a dictum ut, dapibus vitae massa. Cras abc@gmail.com vel libero felis. In augue elit, porttitor nec molestie quis, auctor a quam. Quisque b2b@money.fr pretium dolor et tempor feugiat. Morbi libero lectus, porttitor eu mi sed, luctus lacinia risus. Maecenas posuere leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam erat volutpat. Donec eleifend felis at leo ullamcorper cursus. Pellentesque id dui viverra, auctor enim ut, fringilla est. Maecenas gravida turpis nec ultrices aliquet.'''

def uloz_emailove_adresy(text: str) -> list:
    """
    Uloz vsechny ocistene emailove adresy ze zadaneho textu.

    Priklad:
    >>> print(uloz_emailove_adresy("Ahoj, tady matous@gmail.com."))
    {'matous@gmail.com'}

    >>> print(uloz_emailove_adresy("Ahoj, tady matous"))
    {}
    """
    return [
        slovo.strip(",.:;")
        for slovo in text.split()
        if "@" in slovo
    ]
# Uloz vystup funkce do promenne
vysledek = uloz_emailove_adresy(text)

# Vytiskni obsah promenne vysledek
print(vysledek)