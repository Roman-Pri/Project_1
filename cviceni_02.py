# zadani: Vytvoří list zamestnanci, který obsahuje hodnoty['František', 'Bruno','Anna', 'Jakub','Klára', 'Anežka','Anežka', 'Anežka'
# ]Ulož poslední index ze zadaného listu zamestnanci do proměnné posledni_index,
# Vypiš jméno na indexu 2 za string: 'Na indexu 2 je: ',
# Vypiš jméno na posledním indexu za string: 'Na  indexu je:',
# vypiš jména od indexu 2 do 5 za string: 'V intervalu od 2 do 5 je:',
# vypiš každý třetí prvek listu zamestnanci počínaje hodnotou 'František' za string: 'Každý třetí člen je:'.

zamestnanci= [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
posledni_index = len (zamestnanci) -1
print ("Na indexu 2 je:", zamestnanci [2])
print ("Na", posledni_index,"indexu je:", zamestnanci [posledni_index])
print ("V intervalu od 2 do 5 je:", zamestnanci [2:6])
print ("Kazdy treti clen je:", zamestnanci [::3])

# 2 ukol - tabulka na vypocet BMI

jmeno = "Martin"
vaha = 80
vyska = 2
bmi = vaha / vyska**2
if bmi < 18.5:
    kategorie = "podvyziva"
elif bmi >= 18.5 and bmi <= 25:
    kategorie = "zdrava vaha"
elif bmi >= 25 and bmi <= 30:
    kategorie = "mirna nadvaha"
elif bmi >= 30 and bmi <= 40:
    kategorie = "obezita"
else:
    kategorie = "tezka obezita"
print (jmeno, "tve BMI je:", bmi, ", coz spada do kategorie:", kategorie, ".")


# 3. ukol - vkladani zamestnancu (procviceni metod)
zamestnanci_01= ["Frantisek", "Anna", "Jakub", "Klara"]
print ("zamestnanci na zacatku:", zamestnanci_01)
zamestnanci_a = zamestnanci_01.copy ()
zamestnanci_a. append ("Bruno")
zamestnanci_a. append ("Anezka")
print ("Nova jmena pridana:", zamestnanci_a)
zamestnanci_b = zamestnanci_01.copy ()
zamestnanci_b. insert (1,"Bruno")
print ("Nova jmena vlozena:", zamestnanci_b)

# 4. ukol - prvni pismeno
#Zapiš všechny proměnné o několik rádků výš
# vytvoř proměnnou cislo_dne a zapiš do ní hodnotu 3,
# ověř, jestli hodnota v cislo_dne je v listu vstupni_cisla,pokud není, vypiš výstup podle vzoru níže,pokud je, vypiš zprávu "Správná vstupní hodnota!"
# dále vytvoř proměnnou den_tydne a pomocí upravené hodnoty v proměnné cislo_dne, naindexuj z proměnné tyden požadovaný den (př. 1 --> "pondělí", 2 --> "úterý")
# ověř, jestli vybraný str v proměnné den_tydne má stejné počáteční písmeno, jako jsou v proměnné vstupni_pismena (ověř opět pomocí upraveného indexu),
# pokud se znaky shodují vypiš "Správné písmeno",.. pokud se znaky neshodují vypiš "Špatné písmeno".

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "u", "s", "c", "p", "s", "n"]
tyden = ["pondeli", "utery", "streda", "ctvrtek", "patek", "sobota", "nedele"]
cislo_dne = 3
if cislo_dne in vstupni_cisla:
    print ("Spravna vstupni hodnota!")
    den_tydne = tyden [cislo_dne - 1]
    if den_tydne . startswith (vstupni_pismena [cislo_dne-1]):
        print ("Spravne pismeno!")
    else:
        print ("Spatne pismeno!")
else:
    print ("Spatna vstupni hodnota!")





