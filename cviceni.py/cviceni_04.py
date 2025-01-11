# prvni cviceni
#Vytvoř proměnnou veta, typu str, která obsahuje hodnotu: "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu",
# proměnnou samohlasky, typu str, která obsahuje 'aeiouáéíóú',
# proměnnou souhlasky, typu str, která obsahuje 'bcčdďfghjklmnňprřsštťvzžcdž',
# proměnnou vysledek, typu dict, který obsahuje klíče "souhlasky" a "samohlasky". 
# Slovník bude evidovat výskyty těchto hodnot,iteraci přes všechny znaky v proměnné veta,pokud znak není ani samohláska, ani souhláska, tak jej přeskoč,pokud je znak samohláska nebo souhláska, inkrementuj ve slovníku vysledek správný klíč,nakonec vypiš konečný stav podle ukázky níže.

# Zadaná proměnná
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

# druhe cviceni
#Zapiš hodnoty do proměnné uvedené výš.sečti všechna sudá čísla a výsledek ulož do proměnné suda,sečti všechna lichá čísla a výsledek ulož do proměnné licha,nakonec získáš rozdíl mezi těmito dvěma součty (proměnná vysledek),zajisti, že výsledek nebude záporné číslo (k tomu by ti mohly pomoci built-in funkce pro numerické typy, zmiňované v první lekci).
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

# treti cviceni
# Zapiš hodnoty do proměnné uvedené výš.ověří jestli jsou proměnné start, stop a delitel datový typ int (pomocí built-in funkce isinstance),pokud jsou int, vypiš oznámení dle ukázky níž,pokud alespoň jeden není int, vypiš oznámení dle ukázky níž a ukonči skript,jestli jsou jednotlivé hodnoty z intervalu dělitelné hodnotou v proměnné delitel, potom je přidej do zadaného seznamu vysledek,po skončení iterace všech hodnot vypiš výsledné hodnoty podle vzoru níže.
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

#ctvrte cviceni
#Pomocí slovníkové komprehence spočítej délky slov v zadané sekvenci.
seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]

delky_slov = {ovoce:len(ovoce) for ovoce in seznam_slov}
print(delky_slov)