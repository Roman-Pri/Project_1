# 1. Aktuální cena zlata
# Cílem této úlohy je získat aktuální cenu zlata z webu Business Insider

bi_url = "https://markets.businessinsider.com/commodities/gold-price"

# Jednotlivé kroky, které program musí obsahovat:
# Zapiš proměnnou uvedenou výše,
# vytvoř funkci ziskej_cenu_zlata, která bude mít jeden parametr url,
# funkce ziskej_cenu_zlata musí nejprve získat HTML strukturu a následně umět rozdělit neopracovný string a vyhledat tag, kde se informace o ceně zlata nachází (nejprve si prohlédní strukturu HTML souboru v prohlížeči),
# ulož výstup z funkce do proměnné cena,
# vypiš hodnotu proměnné cena.

import requests
from bs4 import BeautifulSoup


# Vytvoř proměnnou 'bi_url'
bi_url = "https://markets.businessinsider.com/commodities/gold-price"

# Vytvoř funkci 'ziskej_cenu_zlata'
def ziskej_cenu_zlata(url: str) -> str:
    odpoved_serveru = requests.get(url)
    rozdeleny_text = BeautifulSoup(odpoved_serveru.content, "html.parser")
    cena_zlata = rozdeleny_text.find(
        "span",
        {"class": "price-section__current-value"}
    ).get_text()
    return cena_zlata


# Ulož výstup funkce do proměnné 'cena'
cena = ziskej_cenu_zlata(bi_url)

# Vypiš hodnotu v proměnné 'cena'
print(cena)


# 2. Trasparenční účty
# Tvým úkolem bude vytvořit skript, který bude umět vyscrapovat data z trasparentního účtu z FIO banky.
# Postup by měl vypadat následovně:
# Vytvoř si proměnnou (buď doporučený transparentní účet nebo si vyber jiný ze seznamu ):
# vytvoř funkci posli_pozadavek_get, která získá ze zadaného URL hrubé HTML jako string. Funkce pracuje s jedním parametrem url,
# vytvoř funkci ziskej_parsovanou_odpoved, která pracuje s jedním parametrem odpoved_serveru. Ten obsahuje navrácenou hodnotu z funkce posli_pozadavek_get a tu následně rozdělí (naparsuje),
# vytvoř funkci vyber_tr_tagy, která vyfiltruje rozdělené hodnoty z funkce ziskej_parsovanou_odpoved. Funkce vrátí pouze sekvenci tagů tr,
# vytvoř funkci rozdel_zahlavi_a_transakce. Tato funkce pracuje s parametrem vsechny_tr_tagy. Nakonec funkce navrátí dvě hodnoty. První hodnota je list se jmény polí a druhá hodnota jsou samotné transakce.
# nakonec hodnoty vypiš podle ukázky níže.

import bs4
import requests


def posli_pozadavek_get(url: str) -> str:
    """
    Vrať odpověd serveru na požadavek typu GET.
    """
    response = requests.get(url)
    return response.text


def ziskej_parsovanou_odpoved(odpoved: str) -> bs4.BeautifulSoup:
    """
    Získej rozdělenou odpověď na požadavek typu GET.
    """
    return bs4.BeautifulSoup(odpoved, features="html.parser")

def vyber_tr_tagy(odpoved_serveru: bs4.BeautifulSoup) -> bs4.element.ResultSet:
    """
    Ze zdrojového kódu stránky vyber všechny tagy "tr".
    """
    return odpoved_serveru.find_all("tr")


def rozdel_zahlavi_a_transakce(trs: bs4.element.ResultSet) -> tuple:
    """
    Vrať z tagů "tr" pouze záhlaví a informace ke všem transakcím.
    """
    zahlavi, *transakce = trs[2:]
    zahlavi: list = zahlavi.get_text().splitlines()[1:]
    return zahlavi, transakce

if __name__ == "__main__":
    url: str =  \
        "https://ib.fio.cz/ib/transparent?a=2801322199&f=01.07.2023&t=03.07.2023"
    odpoved = ziskej_parsovanou_odpoved(posli_pozadavek_get(url))
    zahlavi, transakce = rozdel_zahlavi_a_transakce(vyber_tr_tagy(odpoved))
    print(transakce)