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

        

