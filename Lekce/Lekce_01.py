# základní aritmetické operace
print(100 + 200)
print(300 - 100)
print(10 * 50)

# všimni si, jak klasické dělení nevrátí celé číslo,..
# ..ale desetinné číslo. Není to žádná chyba,..
# ..ale záměrný účel tohoto operátoru
print(700 / 350)

# pokud chceš ověřit, že jde skutečně o datový typ celých čísel,..
# ..vyzkoušej funkci type
print("Zkousim funkci type")
print(type(100))

# sčítání desetinných čísel
print(0.1 + 0.1)

# odčítání desetinných čísel
print(1.5 - 0.3)

# pomocí funkce type zkoušíme, jaký je číslo 1.3 datový typ
print("Test datoveho typu u cisla 1.3. Datovy typ je:")
print(type(1.3))

#plovouci radova carka
print(0.1 + 0.2)

#celociselne deleni
print(10 // 3)
print(11 // 2)

#modulo
print(10 % 3)
print(11 % 3)

#umocnovani
# hodnota dva na druhou
print(2 ** 2)

# hodnota dva na třetí
print(2 ** 3)

# celočíselné dělení
print("Vytisknu vysledek z celociselneho deleni")
print(10 // 3)

# modulo (zbytek po dělení)
print("Vytisknu vysledek z modula, tzn. zbytek po deleni")
print(4 % 3)

# umocňování (2 ** 3 je hodnota dva na třetí)
print("Vytisknu vysledek z umocneni dva na treti")
print(2 ** 3)

#priority operatoru
print(2 + 3 * 2)

print(2 + 3*2) #moznost vynechani mezer u operatoru s vyssi prioritou

print(2 + (3 * 2)) #uprava pomoci zavorek - nejlepsi reseni

# STRING - zapisujeme string pomocí dvojitých uvozovek
print("Python")

# použijeme funkci type
print(type("Python"))

print("Marian")

# míň používaná varianta
print("""Marian""")

# Pouze textové znaky
print("Python")

# .. funguje i s číslem
print("Python3")

# .. s desetinným číslem
print("Python3.9")

# ověříme, že i čísla v uvozovkách jsou string
print(type("12345"))

# taky další znaky jsou string
print(type("@#!"))

#komplikace se stringy
# tento kód vypíše chybu
#   print("It"s friday")

print("It's friday") # mo6nost ze zmenou uvozovek

# tento kód ti znovu vypíše chybu
#   print("It's "kind of" friday")

#pouziti spec.znaku \
print("It\'s \"kind of\" friday")

#spojovani stringu
print("Prvni" + "Druhy")
print("123" + "456")
print("+" + "-" + "*" + "/")

#opakovani stringu
print("M" * 10)
print("opakujeme" * 3)

#Indexovani
# index 1 ti vypíše druhý znak
print("autobus"[1])

print("autobus"[0])
print("autobus"[1])
print("autobus"[2])
print("autobus"[3])


print("autobus"[-1])
print("autobus"[-2])
print("autobus"[-3])

#Slicing
# chci jen první 4 znaky slova autobus
print("autobus"[0:4])

print("autobus"[0:6])
print("autobus"[1:7])

# první dvě písmena
print("autobus"[0:2]) 

# první dvě písmena, ale zápis jedním číslem
print("autobus"[:2]) 

# od třetího písmena do konce
print("autobus"[2:7]) 

# od třetího písmena do konce, zápis jedním číslem
print("autobus"[2:])

#Striding
print("autobus"[0:7:2])

# chceme začít indexem 1
print("autobus"[1:7:2])

print("autobus"[::2])

# obrácené pořadí, začne "s", jeden znak za druhým
print("autobus"[::-1]) 

# obrácené pořadí, začne "s", poté každý druhý znak
print("autobus"[::-2]) 

# obrácené pořadí, začne "s", poté každý třetí znak
print("autobus"[::-3])

#Promenna
jmeno = "Lukas"

# tvorba proměnné jmeno s hodnotou Lukas
jmeno = "Lukas"

# použití proměnné
print(jmeno)

# proměnná jmeno obsahuje jen písemné znaky
jmeno = "Lukas"

# obsahuje i číselné znaky
jmeno2 = "Matous"

# obsahuje podtržítko
moje_jmeno = "Jan"

# jestli chceme proměnné vypsat, použijeme funkci print
print(jmeno)
print(jmeno2)
print(moje_jmeno)

# proměnná nemůže začínat číslem, vypíše chybu
#  2jmeno = "Marek"
#  print(2jmeno)

# proměnná obsahuje nesprávně mezeru
#  moje jmeno = "Tomas"
#  print(moje jmeno)

# proměnná obsahuje znak @
#  moje@jmeno = "Zdenek"
#  print(moje@jmeno)

#spravny zapis CamalCase
mojeJmeno = "Matous"
novaHodnota = 1234

#spravny zapis Snake_case
moje_jmeno = "Matous"
nova_hodnota = 1234

#zapis na nemennou promenou (cely nazev velkymi pismeny)
TIHOVE_ZRYCHLENI = 9.81
PI = 3.141

#prace s promennymi
jedno_cislo = 5
druhe_cislo = 6
print(jedno_cislo + druhe_cislo)

jmeno = "Karel"
prijmeni = " Novak"
print(jmeno + prijmeni)

#Sekvence - list
# tvůj první list
print(["Matous", "Marek", "Lukas"])

# můžeš si ověřit, jestli máme datový typ list
print(type(["Matous", "Marek", "Lukas"]))

#vytvoreni Listu
# takhle vytvoříš list dle 1. možnosti
prvni_seznam = []

# takhle vytvoříš list dle 2. možnosti
druhy_seznam = list()

# ověř, že obě možnosti vyprodukovali datový typ list
print(type(prvni_seznam))
print(type(druhy_seznam))

#vytvoreni neprazdneho listu
# listy, které obsahují číselné hodnoty
treti_seznam = [2, 4, 6, 8, 10]
ctvrty_seznam = [1.0, 3.0, 5.0, 7.0, 9.0]

# pomocí funkce print si hodnoty v listech můžeš vypsat
print(treti_seznam)
print(ctvrty_seznam)

# prace s listy
muj_seznam = ["Matous", "Marek", "Lukas"]
# chceš si vypsat první hodnotu z muj_seznam, index 0
print(muj_seznam[0])

# vypiš druhou hodnotu s indexem 1
print(muj_seznam[1])

# vypiš poslední hodnotu v listu, s indexem -1
print(muj_seznam[-1])

# poslední hodnota je třetí hodnota v listu
# takže jméno Lukas vypíše i index 2
print(muj_seznam[2])

#Sekvence - TUPLE
print(("Matous", "Marek", "Lukas"))

#vytvoreni TUPLE
# vytvoř tuple pomocí prázdných kulatých závorek
prvni_tupl = ()

# vytvoř tuple pomocí zabudované funkce
druhy_tupl = tuple()

# ověř si datový typ prvního tuplu
print(type(prvni_tupl))

# ověř datový typ druhého tuplu
print(type(druhy_tupl))

#Tuple neprazdny
treti_tupl = ("Praha", "Berlin", "Viden", "Bratislava")

# pozor, tuple můžeš vytvořit i bez kulatých závorek
# ..není to bežné, ale budeš vědět, že to existuje
ctvrty_tupl = 1.3, 3.6, 1.8, 0.4, 1.9

print(type(treti_tupl))
print(type(ctvrty_tupl))

#prace s TUPLY
treti_tupl = ("Praha", "Berlin", "Viden", "Bratislava")
# vypiš první hodnotu z tuplu, tedy index 0
print(treti_tupl[0])

# vypiš poslední hodnotu z tuplu (použij index -1)
print(treti_tupl[-1])

# vypiš jen první dvě hodnoty
print(treti_tupl[0:2])

# vypiš předposlední hodnotu
print(treti_tupl[-2])

## FUNKCE ##
# když spustíš tento kód, neuvidíš žádný výstup
type("abc")

# type("abc") ti určí datový typ hodnoty, která je v závorkách
# funkci print použij, ať uvidíš výstup z editoru
print(type("abc"))

# ..stejně jako u desetinných čísel
print(type(3.1416))

# ..nebo listu
print(type(["m", "h"]))

# do proměnné muj_typ si uložíš výsledek funkce type
muj_typ = type("@")

# pokud chceš výsledek vypsat, použij funkci print
print(muj_typ)

#funkce PRINT
# vypiš celé číslo - int
print(12)

# vypiš text - string
print("Ahoj, tady Matous")

# ulož float do proměnné a vypiš ho
desetinne_cislo = 2.718
print(desetinne_cislo)

jmeno = "Matous"
vek = 99
print("Jmenuji se", jmeno, ". Je mi", vek, "let.")

#INPUT
jmeno = input("Zadej jméno:")

# uloženou hodnotu v proměnné pak vypíšeme
print(jmeno)

# můžeš ji vypsat i s nějakým textem
print("Tvé jméno je:", jmeno)   # vystup z input je vzdy STR

# i když vidíš zadané číslo na výstupu, je to datový typ string
cislo = input("Zadej číslo:")
print("Bylo zadané číslo:", cislo)

# jestli je výstup funkce input string si můžeš ověřit
print(type(cislo))

# pomocí funkce int nastavíš, že hodnota bude datového typu int
cislo_int = int(input("Zadej číslo:"))
print(cislo_int)

# ověř, jestli je cislo_int vážně datový typ int
print(type(cislo_int))

#HELP
# Pro vypsání help(str) použij print
print(help(print))

#ROUND
# zaokrouhli číslo 0.33333 na 2 desetinná místa
print(round(0.33333, 2))

# ..na 4 místa
print(round(0.987654, 4))

# ..a opět na 2 místa
print(round(2.675, 2))

#ABS
print(abs(-1))
print(abs(-1.1234))
print(abs(223))

#INT
# převeď float na int
print(int(1.11))

# převeď string na int
print(int("11"))

#FLOAT
# z celého čísla (int) udělej desetinné
print(float(12))

# string převeď na float
print(float("1.12"))

#STRING
# z int udělej string
print(str(12))

# z float udělej string
print(str(1.12))

#LIST
# vytvoř list ze stringu
print(list("abc"))

# vypiš prázdný list
print(list())

# do proměnné ulož dva stringy a vypiš list
muj_tupl = ("a", "b")
print(list(muj_tupl))

#MIN
# vypiš nejmenší údaj z čísel 1, 2, 3
print(min(1, 2, 3))

# funkce min jde použít i na stringy 
# - jenom pozor, občas nemusí vrátit, co bys čekal
print(min("karel"))
print(min("Karel"))

#LEN
# kolik znaků má string abc?
print(len("abc"))

# délka prázdného listu
print(len([]))

# délka listu s 5 hodnotami
print(len(list("abcde")))

#MAX
# najdi největší hodnotu
print(max(11, 12, 13, 13, 14, 14))

# stejně jako min, i funkce max jde použít i na stringy 
# - jenom pozor, občas nemusí vrátit, co bys čekal
print(max("ZuZka")) #vyhledem k velikosti ASCII hodnot
print(max("zuzka"))

#TUPLE
# ze stringu vytvoř tuple
print(tuple("abc"))

# vypiš prázdný tuple
print(tuple())

# v proměnné máš uložený list
# tento list pomocí funkce předělej na tuple
muj_seznam = ["a", "b"]
print(tuple(muj_seznam))