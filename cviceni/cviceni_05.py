#V této úloze vytvoř program, který ukládá slova, která mají délku čtyři znaky. Jakmile uloží tři taková slova, skončí.
#1]Definuj novou proměnnou slova, kam budeš slova ukládat,
#2]zapiš proces, který ukládá ukládá vstupy uživatele do proměnné slovo,
#3]tento proces pracuje tak dlouho, dokud proměnná slova neobsahuje tři unikátní slova,
#4]pokud je uživatelem vybrané slovo již součástí objektu slova, potom vypiš zprávu "Slovo  už je uložené",
#5]pokud není uživatelem vybrané slovo dlouhé čtyři znaky, vypiš zprávu "Slovo není dlouhé čtyři znaky",
#6]pokud je uživatelem vybrané slovo dlouhé čtyři znaky, potom jej přidej do proměnné slova,
#7]jakmile proces skončí (proměnná slova obsahuje tři hodnoty), vypiš zprávu "Už mám uložené tři slova".

slova = set()

while len(slova) < 3:
    slovo = input("Zadej slovo o čtyřech znacích: ")

    # délka vstupu
    if len(slovo) != 4:
        print("Slovo není dlouhé čtyři znaky. Zkus to znovu.")
        continue

    # Zkontrolujeme, jestli je slovo již uloženo (case-insensitive)
    if slovo.upper() in slova:
        print(f"Slovo '{slovo.upper()}' už je uložené!")
    else:
        slova.add(slovo.upper())  # Uložíme převedené slovo

print("Už mám uložené tři slova:", ", ".join(slova))


# V této úloze vytvoř program, který uživateli umožní vybrat ze zadaných hodnot.
# Pokud zapíše cokoliv jiného, program jej upozorní a nechá jej vybírat tak dlouho, dokud nezadá validní hodnotu.
# Jednotlivé kroky, které program musí obsahovat:
# 1.Definovat objekt ovoce, který obsahuje unikátní stringy "jablko", "banan", "citron", "pomeranc",
# 2.vypsat uživateli všechno uložené ovoce v proměnné ovoce spojené znaky ", ",
# 3.vybrat si ovoce z nabídky pomocí funkce input do proměnné vyber s ohlášením "VYBER Z DOSTUPNÉHO OVOCE:",
# 4.pokud si uživatel nevybere z nabídky, vypsat: "Ovoce není v nabídce." a nechat jej vybírat tak dlouho, pokud nezadá jeden ze stringů v proměnné ovoce,
# 5.pokud si uživatel vybere jednu z možností v ovoce, potom program vypíše "Bezva, toto ovoce je v nabídce.".
    
ovoce =  {"jablko", "banan", "citron", "pomeranc"}
print(f"Dostupne ovoce: {", ".join(ovoce)}")
while True:
    vyber = input("VYBER Z DOSTUPNÉHO OVOCE:")
    if vyber not in ovoce:
        print("Ovoce není v nabídce.")
    else:
        print("Bezva, toto ovoce je v nabídce.")
        break

        
#V této úloze vytvoř program, který si od uživatele nejprve vyžádá aritmetický operátor a následně čísla, se kterými celý zápis vypočítá.
#Po každé operaci se program uživatele zeptá zda chce provést další operaci nebo chce program ukončit.
#Jednotlivé kroky, které program musí obsahovat:
#1.Vytvoř nekonečnou smyčku,
#2.uživatel může vybrat operátor, dostupné jsou "+", "-",
#3.vstup uživatele ulož do proměnné operation,
#4.pokud hodnota v proměnné operation není ("+", "-"), vypiš "Nezadali jste platný operátor, zkuste to znovu" a vrátí se na začátek běhu programu,
#5.pokud je hodnota v proměnné - ("+", "-"), dovol uživateli zadat vstupy do proměnných number_1 a number_2,
#6.spoj hodnoty v number_1, choice a number_2, vypočítej výsledek a vypiš např. 1 + 9 = 10,
#7.zeptá se uživatele zda chce provést další operaci pokud ano program se vrátí na začátek běhu, pokud ne program se ukončí.

while True:

    # Zapiš výběr operace, kterou kalkulačka disponuje
    operation = input('''
Sčítání:    "+",
Odčítání:   "-",
----------------------
Vyber si operaci: '''
                )

    # Ověř zda uživatel zvolil platný operátor
    if operation not in ('+','-'):
        print('Nezadali jste platný operátor, zkuste to znovu.')
        continue

    # Získej čísla pro výpočet od uživatele
    number_1 = int(input('Zadej první číslo: '))
    number_2 = int(input('Zadej druhé číslo: '))

    # Dle operátoru proveď výpočet a vypiš ho
    if operation == '+':
        print(f'{number_1} + {number_2} = {number_1 + number_2}')
    
    elif operation == '-':
        print(f'{number_1} - {number_2} = {number_1 - number_2}')

    # Ověř zda chce uživatel pokračovat nebo chce program ukončit
    again = input('Chcete provést další operaci?(a pro ano, jakákoliv jiná klávesa pro ne): ')

    if again == 'a':
        continue
    else:
        print(
'Ukončuji...')
        break