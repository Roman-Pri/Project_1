#Try/except
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
        print(vysledek)

    except TypeError:
        print("Nemůžeš dělit string")
    
    
for cislo in (1, 2, 3, "4", 5):
    vrat_vysledek(cislo, 2)
    
#Try/except/except
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
        print(vysledek)
    # první výjimka
    except TypeError:          
        print("Nemůžeš dělit string")
    # druhá výjimka
    except ZeroDivisionError:  
        print("Nemůžeš dělit nulou")
    
    
for cislo, delitel in zip((1, 2, 3, "4", 5), (1, 2, 0, 3, 4)):
    vrat_vysledek(cislo, delitel)

# sdruzeny zapis - nevyhodny
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
        print(vysledek)
    # sdružený zápis
    except (TypeError, ZeroDivisionError):  
        print("Problémy při dělení")
   
    
for cislo, delitel in zip((1, 2, 3, "4", 5), (1, 2, 0, 3, 4)):
    vrat_vysledek(cislo, delitel)

#Try/except/else
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
    # první výjimka
    except TypeError:          
        print("Nemůžeš dělit string")
    # druhá výjimka
    except ZeroDivisionError:  
        print("Nemůžeš dělit nulou")
    # proveď pouze bez výjimek
    else:                     
        print(vysledek)
    
    
for cislo, delitel in zip((1, 2, 3, "4", 5), (1, 2, 0, 3, 4)):
    vrat_vysledek(cislo, delitel)

#Try/except/else/finnaly
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
    # první výjimka
    except TypeError:          
        print("Nemůžeš dělit string")
    # druhá výjimka
    except ZeroDivisionError:  
        print("Nemůžeš dělit nulou")
    # proveď pouze bez výjimek
    else:                      
        print(vysledek)
    # proveď pokaždé
    finally:                   
        print("..zpracováno")
    
    
for cislo, delitel in zip((1, 2, 3, "4", 5), (1, 2, 0, 3, 4)):
    vrat_vysledek(cislo, delitel)

#odstranovani chyb
def formatuj_jmeno(string, symbol: str = ".") -> tuple:
    """
    :Priklad:
    >>> rozdel_string("marek.parek")
    'Marek'
    """
    # chybí index 0, pro jméno
    jen_jmeno = string.split(symbol)  
    return jen_jmeno.title()


def vytvor_pozdrav(jmeno: str) -> str:
    """
    :Priklad:
    >>> vytvor_pozdrav("marek.parek")
    'Toto je Marek, zdravíme!'
    """
    return f"Toto je {formatuj_jmeno(jmeno)}, zdravíme!"


print(vytvor_pozdrav("petr.svetr"))

#odstranovani chyb pomoci print
def formatuj_jmeno(string, symbol: str = ".") -> tuple:
    """
    :Priklad:
    >>> rozdel_string("marek.parek")
    'Marek'
    """
    # chybí index 0, pro jméno
    jen_jmeno = string.split(symbol)  
    # doplněná funkce 'print'
    print(jen_jmeno)                  
    return jen_jmeno.title()


def vytvor_pozdrav(jmeno: str) -> str:
    """
    :Priklad:
    >>> vytvor_pozdrav("marek.parek")
    'Toto je Marek, zdravíme!'
    """
    return f"Toto je {formatuj_jmeno(jmeno)}, zdravíme!"

print(vytvor_pozdrav("petr.svetr"))

# debug ve visual code
def projdi_udaje(*args) -> list:
    for udaj in args:
        if "quit" in udaj.lower():
            break
        else:
            jmeno, domena = udaj.split("@")
            print(
                {
                    "jmeno": jmeno,
                    "domena": domena
                }
            )


projdi_udaje(
    'p.fulinova@firma.cz',
    'a.vancurova@firma.cz',
    'a.hertlova@firma.cz',
    'p.vyhnis@firma.cz',
    'j.feckanin@firma.cz',
    'p.harant@firma.cz',
    'm.miczova@firma.cz',
    'j.mosquito@firma.cz',
    'b.suvova@firma.cz',
    'l.kafkova@firma.cz',
    'n.hoffmannova@firma.cz',
    'd.sedlakova@firma.cz',
    'i.jerabkova@firma.cz',
    'v.jagerska@firma.cz',
    'h.bayerova@firma.cz',
    't.zamecnik@firma.cz',
    'h.strasilova@firma.cz',
    'j.kralova@firma.cz',
    'h.duskova@firma.cz',
    'd.mirgova@firma.cz',
    "quit"
)