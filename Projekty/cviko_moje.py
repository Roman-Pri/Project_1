import re

# Seznam registrovaných uživatelů (jméno a heslo)
registrovani_uzivatele = {
    "jan": "heslo123",
    "petr": "tajneheslo",
    "lucie": "mojeheslo"
}

# Předdefinované texty k analýze
texty = [
    "Toto je první text k analýze. Obsahuje jednoduchá slova.",
    "Druhý text je o něco delší a obsahuje více informací a složitější věty.",
    "Třetí text je ještě složitější. Je plný různých slov a znaků! Obsahuje čísla jako 42 a 100."
]

# Funkce pro analýzu textu
def analyzuj_text(vybrany_text):
    print("\nTextová analýza")

    slova = vybrany_text.split()
    pocet_slov = len(slova)
    pocet_velky_pocatecni = sum(1 for slovo in slova if slovo[0].isupper())
    pocet_velkymi_pismeny = sum(1 for slovo in slova if slovo.isupper())
    pocet_malymi_pismeny = sum(1 for slovo in slova if slovo.islower())
    
    # Najít čísla a spočítat jejich součet
    cisla = [int(cislo) for cislo in re.findall(r'\b\d+\b', vybrany_text)]
    pocet_cisel = len(cisla)
    suma_cisel = sum(cisla)

    print(f"Počet slov: {pocet_slov}")
    print(f"Počet slov začínajících velkým písmenem: {pocet_velky_pocatecni}")
    print(f"Počet slov psaných velkými písmeny: {pocet_velkymi_pismeny}")
    print(f"Počet slov psaných malými písmeny: {pocet_malymi_pismeny}")
    print(f"Počet čísel: {pocet_cisel}")
    print(f"Suma všech čísel: {suma_cisel}")

# Hlavní část programu
def hlavni_program():
    uzivatel = input("Zadejte přihlašovací jméno: ")
    heslo = input("Zadejte heslo: ")

    if uzivatel in registrovani_uzivatele and registrovani_uzivatele[uzivatel] == heslo:
        print(f"\nVítejte, {uzivatel}!")
        
        while True:
            print("\nDostupné texty k analýze:")
            for i, text in enumerate(texty, 1):
                print(f"{i}. Text {i}")

            try:
                volba = int(input("\nZadejte číslo textu, který chcete analyzovat: "))
                if 1 <= volba <= len(texty):
                    analyzuj_text(texty[volba - 1])
                else:
                    print("\nNeplatná volba. Program se ukončuje.")
                    break
            except ValueError:
                print("\nNeplatný vstup. Očekáváno číslo. Program se ukončuje.")
                break

            dalsi_analyza = input("\nChcete analyzovat další text? (ano/ne): ").strip().lower()
            if dalsi_analyza != 'ano':
                print("\nDěkujeme za použití programu. Nashledanou!")
                break
    else:
        print("\nNeplatné přihlašovací údaje. Program se ukončuje.")

# Spuštění programu
if __name__ == "__main__":
    hlavni_program()
