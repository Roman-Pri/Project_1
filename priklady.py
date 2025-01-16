# soucet zadanych cisel
prvni_zadane_cislo = int (input ("Zadej prvni cislo:"))
druhe_zadane_cislo = int (input ("Zadej druhe cislo:"))
print ("Soucet zadanych cisel je:", prvni_zadane_cislo + druhe_zadane_cislo)

# rozpoznani sudych a lichych cisel
zadane_cislo = int (input ("Zadej jakekoliv cele cislo:"))
if zadane_cislo % 2 == 0 :
    print  ("Zadane cislo", zadane_cislo, "je sude.")
else:
    print ("Zadane cislo", zadane_cislo, "je liche.")
    
muj_slovnik = {"klic":"hodnota"}
muj_slovnik ["seznam"] = "ahoj"
email = {"email":"roman@gmail.com"}
muj_slovnik.update (email)
print(muj_slovnik)
seznam_01= muj_slovnik.copy ()
print(seznam_01)

print(bool(False or True and False))


for word in (1,2,3,4,5):
    print(word)

for vypis in {"jmeno":"Roman", "vek": 134}:
    print(vypis)

velka_pismena_na_zacatku = list()

for slovo in ("Roman", "petr", "Jana", "petra"):
    if slovo.istitle():
        velka_pismena_na_zacatku.append(slovo)
        print (velka_pismena_na_zacatku)


#hraju si - vytazky ze seznamu
mix_pismen = list()
mix_cisel = list()

for extrakt in ["1","w","3","f","r","4","5","h","4","3","4","904","456","fgh","wer"]:
    if extrakt.isalpha():
        mix_pismen.append(extrakt)
    elif extrakt.isnumeric():
        mix_cisel.append(extrakt)
else: print (mix_pismen), print (mix_cisel)


for cislo in range(1,20):
    if cislo % 2 ==0:
        continue
    elif cislo>10:
        print("prvni liche cislo po 10:", cislo)
        break

seznam_02 = [
        ["Petr", "Pavel", "Sona"],
        ["Jolana", "Igor", "Jitka"],
        ["Lenka", "Petra", "Silva"]
]
# vytiskne cely prvni list jako list
print (seznam_02[1])

#vypsat prvni list
for list in seznam_02[1]:
       print(list)


#vypsat cely
for vnoreny in seznam_02:
    for jmeno in vnoreny:
        print(jmeno)

rozsah = range(11)
print(rozsah)
#enumerate
print(tuple(enumerate(seznam_02)))

for list in seznam_02[1]:
    for jmena in list:
        print(tuple(enumerate(jmena)))


for list in enumerate ("jdi do prdele"):
    print(list)


seznam_03 = ["Petr", "Pavel", "Sona", "Jolana", "Igor", "Jitka", "Lenka", "Petra", "Silva"]

print(tuple(enumerate(seznam_03)))


vysledek = []

for pismeno in "Roman":
    vysledek.append(pismeno)
    print(vysledek)

#komprehence

vysledek_01 = [pismeno.upper() for pismeno in  "Matous"]
print(tuple(enumerate(vysledek_01)))


vstup_pro_vzorec = (5,3,6,9,10)

#komprehence do slovniku
vypocet = {vstup:(vstup+5)*8 for vstup in vstup_pro_vzorec}
print(f"dict:{vypocet}")

#komprehence do setu

seznam_jmena = {jmena.title() for jmena in "roman petr Pavel".split()}
print(seznam_jmena)

# 4 cviceni znovu
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'

vysledky = {"samohlasky":0, "souhlasky":0}
samohlasky = "aeiouáéíóúů"
souhlasky = "bcčdďfghjklmnňprsštťvzžxwy"


for pismeno in veta:
    if not pismeno.isalpha():
        continue
    elif pismeno.lower() in samohlasky:
        vysledky["samohlasky"] = vysledky["samohlasky"] + 1 #lehka verze souctu cisel a pridani do promenne
    elif pismeno.lower() in souhlasky:
        vysledky["souhlasky"] += 1                          # zkracena verze souctu cisel a pridani a pridani do promenne
print(f"Pocet souhlasek: {vysledky["souhlasky"]} | Pocet samohlasek: {vysledky["samohlasky"]}")


# listova komprehence
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'

samohlasky = "aeiouáéíóúů"
souhlasky = "bcčdďfghjklmnňprsštťvzžxwy"

vysledky = {
    "samohlasky": sum(1 for pismeno in veta if pismeno.isalpha() and pismeno.lower() in samohlasky),
    "souhlasky": sum(1 for pismeno in veta if pismeno.isalpha() and pismeno.lower() in souhlasky)
}

print(f"Pocet souhlasek: {vysledky['souhlasky']} | Pocet samohlasek: {vysledky['samohlasky']}")

# suda licha jejich soucet a spolecny rozdil
cisla_sez = [1, 2, 3, 4, 5, 6, 7, 8]

licha_cisla = 0
suda_cisla = 0


for cislo in cisla_sez:
    if cislo%2== 0:
        suda_cisla += cislo  # nebo lehceji suda = suda + cislo
    elif cislo%2!= 0:
        licha_cisla += cislo  # nebo lehceji licha = licha + cislo
else:
    promenna_vysledek = (abs(suda_cisla - licha_cisla))
    print("Rozdil je:", promenna_vysledek)

#zajimavy priklad
vysledek_05 = []
start = 345
stop = 456
delitel = 5

if isinstance(start,int) \
    and isinstance(stop,int)\
    and isinstance(delitel,int):
    print(f"Zadany rozsah: <{start}, {stop}>")
    for cislo in range(start,stop +1):
        if cislo % delitel == 0:
            vysledek_05.append(cislo)
    print(f"Cisla delitelna {delitel}: {vysledek_05}")
else: print("Zadane vstupy musi byt cisla!")


# vytiskni slovnik s delkou slov ze seznam_slov
seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]

delky_slov = {ovoce:len(ovoce) for ovoce in seznam_slov}
print(delky_slov)



#s lektorem
emails = [
    "m.vybiralova@firma.cz",
    "m.vybiralova@email.cz",
    "m.vybiralova@dobradomena.cz",
    "marie@vybiralova.cz",
    "marie.vybiralova@gmail.com",
]
domeny = []
for email in emails:
    domena = email.split("@")[1].split(".")[0]
    domeny.append(domena)
sorted
print(domeny)




