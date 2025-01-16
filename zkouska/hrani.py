import random
import time

czech_first_names = ["Jan", "Petr", "Jiří", "Pavel", "Martin", "Tomáš", "Jaroslav", "Miroslav", "Zdeněk", "Václav", "Karel", "Josef", "Lukáš", "Milan", "Roman", "Aleš", "Ivana", "Martina", "Lenka", "Jana"]

czech_surnames = ["Novák", "Svoboda", "Novotný", "Dvořák", "Černý", "Procházka", "Kučera", "Veselý", "Horák", "Němec", "Marek", "Pospíšil", "Pokorný", "Hájek", "Král", "Jelínek", "Růžička", "Beneš", "Fiala", "Sedláček"]

def gener(czech_first_names, czech_surnames):
    """ ddwew"""

    Args:
        czech_first_names (_type_): _description_
        czech_surnames (_type_): _description_

    Returns:
        _type_: _description_
    """
    zamestnanec = {}
    zamestnanec["zamestnanec_id"] = random.randint(0, 1000)
    zamestnanec["jmeno"] = random.choice(czech_first_names)
    zamestnanec["prijmeni"] = random.choice(czech_surnames)
    zamestnanec["vytvoreno"] = time.strftime("%m/%d/%Y", time.localtime(time.time() - 606024 * random.randint(1, 365)))
    return zamestnanec

print(gener(czech_first_names, czech_surnames))








