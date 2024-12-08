# lekce 4
muj_seznam = [1, 2, 3, 4, 5]
# chci vypsat každou hodnotu z listu
print(muj_seznam[0])
print(muj_seznam[1])
print(muj_seznam[2])
print(muj_seznam[3])
print(muj_seznam[4])

# vyuziti FOR cyklu pro stejny ukol s listy (cisel a pismen)
for cislo in [1, 2, 3, 4, 5]:
   print(cislo)

for pismeno in ["a", "b", "c", "d"]:
   print(pismeno)

#ukazka neiterovanych datovych typu (int, float, str) - nelze je smyckovat
for cislice in 1234:
   print(cislice)

for cislice in 3.1415:
   print(cislice)

for pismeno in "abcd":
   print(pismeno)

#ukazka iterovanych datovych typu (list, tuple, dict, set)
for pismeno in ("a", "b", "c", "d"): #Datový typ tuple, stejně jako jemu blízký list, můžeme také iterovat. Smyčka for bude fungovat i tehdy, pokud tebou zadaný tuple nebo list budou obsahovat celá či desetinná čísla.
   print(pismeno)

for klic in {"jmeno": "Matous", "vek": 100, "email": None}: #Také skrze datový typ dict je možné iterovat. Můžeš si všimnout, že v každém kroce smyčka přirazuje jména klíčů ("jmeno", "vek" a "email").
   print(klic)

for symbol in {"#", "$", "%", "&"}:  #Dále je možné projít i hodnoty v datovém typu set. Podívej se na pořadí, jak jsou hodnoty v setu zapsané a v jakém jej smyčka for s funkcí print vypisuje. Vzpomeň si na pravidlo, že set nemá pořadí.
   print(symbol)

#podminky ve smycce
suda_cisla = list()

for cislo in (1, 2, 3, 4, 5):
    if cislo % 2 == 0:      # pokud je hodnota v proměnné "cislo" sudá
        suda_cisla.append(cislo)  # ... přidej ji do seznamu "suda_cisla"

# po skončení smyčky vypíšeme obsah proměnné 'suda_cisla'
print(suda_cisla)

for cislo in (1, 2, 3, 4, 5):
    if cislo % 2 == 0:
        print("Sude cislo")    #s elif a else
    elif cislo % 2 != 0:
        print("Liche cislo")

# ohlaseni ve smyckach
for pismeno in ("a", "b", "c", "d"):
    if pismeno == "c":
        print("Nasel jsem 'c', preskakuji cyklus..")
        break
    print(pismeno)

for pismeno in ("a", "b", "c", "d"):
    if pismeno in {"a", "b"}:
        continue
    print("Hodnota", pismeno, "je dulezita")

# For&else
for pismeno in ("a", "b", "c", "d"):
    print(pismeno.upper())
else:
    print("Vsechna pismena vypsana")



for pismeno in ("a", "b", "c", "d"):
    if pismeno == "c":
        print("Nasel jsem 'c', preskakuji cyklus..")
        break
else:
    # kvůli 'break' se tento text nevypíše po ukončení smyčky
    print("Vsechna pismena vypsana")

print("Pokracuji po smycce")

# zanorena smycka
jmena = [
    ["Matous", "Marek", "Lukas", "Jan"],
    ["Lucie", "Aneta", "Eva", "Lenka"],
    ["Helmut", "Hammet", "Hetfield", "Harold"]
]

for jmeno in jmena:
    print(jmeno)



for seznam in jmena:
    for jmeno in seznam:   #zanorena smycka
        print(jmeno)