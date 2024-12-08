# ukol na rozcviceni 
# Program slouží jako rezervační systém dovolenkového portálu. 
# Pro testovací provoz se vytvořilo 5 testovacích účtů. 
# Pomocí těchto účtu je možné se přihlásit do systému. 
# Po příhlášení systém pozdraví uživatele a dá mu na výběr z destinací. 
# Poté mu dovolí zadat místo A a místo B. Následně mu vypíše vzdálenost mezi městy.

usernames = ["Petr", "Jan", "Pavel", "Kristyna", "Helena"]
passwords = ["Heslo1", "Heslo2", "Heslo3", "Heslo4", "Heslo5"]

cities = [
    'Brno',
    'Plzeň',
    'Olomouc',
    'Liberec',
    'České Budějovice',
    'Hradec Králové',
    'Ústí nad Labem',
    'Pardubice',
    'Zlín',
    'Ostrava',
    'Karlovy Vary',
    'Jihlava',
    'Praha',
    'Paskov',
    'Kladno'
]
distances = [
    [0, 296, 77, 307, 216, 168, 296, 146, 96, 169, 337, 93, 208, 176, 240],
    [296, 0, 369, 200, 137, 208, 181, 213, 388, 462, 81, 217, 92, 469, 100],
    [77, 370, 0, 236, 290, 139, 370, 135, 63, 98, 411, 167, 282, 104, 314],
    [309, 198, 237, 0, 249, 98, 96, 155, 401, 434, 233, 230, 110, 449, 135],
    [217, 137, 290, 250, 0, 253, 239, 258, 309, 383, 218, 138, 151, 389, 183],
    [167, 209, 140, 97, 253, 0, 190, 24, 206, 238, 240, 112, 116, 245, 143],
    [298, 181, 371, 96, 238, 190, 0, 196, 390, 463, 122, 219, 93, 470, 87],
    [146, 214, 135, 154, 193, 24, 196, 0, 201, 234, 246, 90, 121, 240, 149],
    [96, 389, 62, 400, 308, 206, 389, 202, 0, 124, 430, 186, 300, 131, 333],
    [170, 463, 94, 440, 383, 239, 463, 235, 125, 0, 504, 261, 375, 14, 407],
    [337, 82, 410, 234, 218, 241, 121, 246, 429, 502, 0, 258, 127, 509, 105],
    [93, 218, 167, 229, 138, 113, 218, 90, 186, 259, 259, 0, 130, 266, 162],
    [209, 91, 282, 109, 150, 116, 92, 121, 301, 375, 128, 130, 0, 382, 31],
    [176, 469, 100, 451, 388, 244, 469, 240, 131, 13, 510, 266, 380, 0, 412],
    [240, 99, 313, 135, 181, 143, 86, 148, 332, 406, 105, 161, 31, 412, 0]
    ]

user = input("Zadej svoje jmeno:")
password = input("Zadej svoje heslo:")

if user in usernames and password in passwords:
    print ("Vitejte na nasem rezervacnim portalu, kde si muzete zmerit vzdalenost mezi stanovenymi mesty!")
    print ("Vyberte si z nasledujiciho seznamu:", str(cities))

    prvni_mesto = input ("Zadej prvni mesto ze seznamu:")
    druhe_mesto = input ("Zadej druhe mesto ze seznamu:")
    if prvni_mesto in cities and druhe_mesto in cities:
        index_a = cities.index(prvni_mesto)
        index_b = cities.index(druhe_mesto)
        print("Vysledna vzdalenost je:", distances [index_a] [index_b], "Km")
    else:
        print("Zadana mesta nejsou vseznamu!")
else:
    print ("konec")
        
# moje slovniky
muj_slovnik = {"typ auta": "audi",
               "rychlost": { "maximalni":200,
                            "prumerna": 100,
                          "minimalni": 0},
                "spotreba": "5l/100"}
print(muj_slovnik)

hockey = {
    "league": "NHL",
    "Teams": 32,
    "Players": [
        {"name": "Rudy Gay", "position": "Center", "goals": 38},
        {"name": "Lewis Carroll", "position": "Left Wing", "goals": 29},
        {"name": "Matt Gasparro", "position": "Defense", "goals": 22},
        {"name": "Dave Carroll", "position": "Goalie", "goals": 0}  
    ]
}

print(hockey["Players"])

# kopie slovniku
uzivatel_3 = {
    "jmeno": "Lukáš",
    "prijmeni": "Holinka",
    "vek": 28,
    "hobby": ("fotbal", "hry", "pratele"),
    "kontakt": {
        "telefon": "000 123 456 789",
        "email": "lukas@gmail.com",
        "web": "www.lukas.cz"
    }
}
uzivatel = uzivatel_3.copy()

#sety
#Úkol:
#  Kdo má svátek jak v lednu tak v unoru?
# Kdo má svátek v lednu ale ne v únoru?
# Kdo má svátek v únoru ale ne v lednu?
# Kdo má svátek jenom v lednu ale nebo jenom v únoru?

leden = ["Nový rok", "Karina / Vasil", "Radmila / Radomil", "Diana", "Dalimil", "Tři králové", "Vilma", "Čestmír",
    "Vladan / Valtr", "Břetislav", "Bohdana", "Pravoslav", "Edita", "Radovan", "Alice", "Ctirad", "Drahoslav",
    "Vladislav / Vladislava", "Doubravka", "Ilona / Sebastián", "Běla", "Slavomír / Slavomíra", "Zdeněk", "Milena",
    "Miloš", "Zora", "Ingrid", "Otýlie", "Zdislava", "Robin / Erna", "Marika",]

unor = ["Nový rok", "Karina / Vasil", "Radmila / Radomil", "Diana", "Dalimil", "Tři králové", "Vilma", "Čestmír",
    "Vladan / Valtr", "Břetislav", "Bohdana", "Pravoslav", "Edita", "Radovan", "Alice", "Ctirad", "Drahoslav",
    "Vladislav / Vladislava", "Doubravka", "Ilona / Sebastián", "Oldřich", "Lenka / Eleonora", "Petr", "Svatopluk",
    "Matěj / Matyáš", "Liliana", "Dorota", "Alexandr", "Lumír", "Horymír"]

print (set(leden) & set(unor)) # prunik (kdo slavi v lednu i v unoru - ti stejni)
print (set(leden) - set(unor)) # rozdil tech co slavi jen v lednu
print (set(unor) - set(leden)) # a tech co slavi jen v unoru
print (set(leden) ^ set(unor)) # jen svatek v lednu a v unoru



