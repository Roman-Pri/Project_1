# Přečti slova
# Vytvoř program, který přečte textový soubor a zobrazí slova, která obsahují 7 a více znaků.
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř si složku, 
# vytvoř v ní soubor slova.txt a main.py,
# do souboru slova.txt ulož obsah uvedený nize,
# v souboru main.py, vytvoř funkci zobraz_slova, která bude mít jeden parameter textovy_soubor,
# funkce zobraz_slova vezme soubor, přečte jeho obsah a vypíše všechny slova, která obsahují 7 a více znaků.

# Otevri textovy soubor v modu cteni
def zobraz_slova(textovy_soubor):
    """
    Vytvor funkci, ktera otevre textovy soubor a precte slova.
    """
    zadana_slova = open(textovy_soubor, "r")

    data = zadana_slova.read()
    slova = data.split()

    for slovo in slova:
        if len(slovo) >= 7:
            print(slovo, end=" ")
    zadana_slova.close()


if __name__ == "__main__":
    zobraz_slova("slova.txt")
    

# 2. Vytvoř textový soubor
# V této úloze si procvičíš zapisování a čtení obsahu textového souboru.
# Nezapomeň, že pro takové zacházení s textovým souborem musíš použít vhodný režim (mód).
# Tvůj zápis musí obsahovat následující:
# Nejdřív zapiš pomocné proměnné uvedené nize,
# následně zapiš zadané proměnné do nového souboru txt_soubor.txt a ulož jej do objektu txt_soubor,
# dále zapiš postupně (nebo zaráz) všechny tři zadané proměnné prvni_radek, druhy_radek a treti_radek,
# po zapsání soubor zavři,znovu soubor otevři a vytvoř pro něj novou proměnnou cteni_txt,
# přečti a ulož jeho obsah do proměnné obsah_txt,nakonec vypiš obsah proměnné obsah_txt pomocí funkce print.

# zapiš pomocné proměnné
prvni_radek = "První řádek v souboru,\n"
druhy_radek = "druhý řádek v souboru,\n"
treti_radek = "třetí řádek v souboru."

# zapiš proměnné do nového txt souboru
txt_soubor = open("txt_soubor.txt", mode="w")
txt_soubor.write(prvni_radek)
txt_soubor.write(druhy_radek)
txt_soubor.write(treti_radek)

txt_soubor.close()

# přečti a ulož obsah txt souboru
cteni_txt = open("txt_soubor.txt")
obsah_txt = cteni_txt.readlines()

# vypiš výsledek
print(obsah_txt)



# 3. Zaokrouhli hodnoty
# Zkus si trochu pohrát s formátováním stringů a s přesností.
# Jaký způsob formátování si vybereš je zcela na tobě.
# Program bude obsahovat tyto kroky:
# Na začátek souboru zapiš tyto proměnné uvedené výš,
# použij proměnnou formatovana_presnost, 
# kam naformátuješ hodnotu v presnost_cisla tak, aby výstup vypadal: |1.23e+02|123.5|123.46|,
# dále zapiš proměnnou formatovana_kombinace, kam naformátuješ hodnotu v kombinace, aby výstup vypadal: |1.234$|,
# nakonec zapiš proměnnou formatovana_presnost_str, kam naformátuješ hodnotu v presnost_str, aby výstup vypadal: |Hell|,
# v neposlední řadě vypiš pomocí funkce print výstup podle vzoru níže a jednotlivé hodnoty zarovnej pomocí tabulátorů,
# obsah proměnných pod sebe zapiš do textového souboru vysledek.txt.

# Vstupní proměnné
kombinace = 1.234
presnost_str = "Hello"
presnost_cisla = 123.4567

# Přesnost pro číselné znaky
formatovana_presnost = \
    f"|{presnost_cisla:.3}|{presnost_cisla:.4}|{presnost_cisla:.5}|"

# Přesnost a ostatní specifikátory
formatovana_kombinace = f"|{kombinace:$<6.4}|"

# Přesnost u stringu
formatovana_presnost_str = f"|{presnost_str:.4}|"

# Výpis hodnot
print(f"""\
Naformátovaná přesnost: \t{formatovana_presnost},
Naformátovaná kombinace: \t{formatovana_kombinace},
Naformátovaný string: \t\t{formatovana_presnost_str}.""")

# Ulož proměnné do souboru 'vysledek.txt'
print("Zapisuji do souboru")

with open("vysledek.txt", mode="w") as txt:
    txt.write("\n".join(
        (formatovana_presnost, formatovana_kombinace, formatovana_presnost_str)
        )
    )