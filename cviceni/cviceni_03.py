# cviceni 1
# vytvoř nový prázdný slovník user_1,
# doplní do slovníku user_1 klíč name (hodnota "Marek") a surname (hodnota "Parek"),
# pomocí vhodné metody rozšíří stávající slovník user_1 o zadanou proměnnou user_email,
# vypiš hodnoty nového slovníku user_1 s úvodním textem "User #01:"

user_email = {"email":"marek.parek@gmail.com"}
user_1 = {}
user_1 ["name"] = "Marek"
user_1 ["surname"] = "Parek"
user_1. update (user_email)
print ("User #01:", user_1)

# cviceni 2
#V této úloze vytvoř program, který se pokusí ověřit, jestli heslo vložené uživatelem patří k jeho účtu.

jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}
if uzivatel.get (jmeno) == heslo:
    print("Ahoj", jmeno, "vitej v aplikaci! Pokracuj...")
else:
    print("Uzivatelske jmeno a heslo nejsou v poradku!")

# cviceni 3 - sjednoceni (union) setu
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
set_1 = set(cisla_1)
set_2 = set(cisla_2)
print(set_2)
sjednocene_hodnoty = set_1.union (set_2)
print ("Sjednocene hodnoty ze zadani:", sjednocene_hodnoty)

# cviceni 4 - rozdil cisel
cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
rozdil_cisel = cisla_1 - cisla_2
print("Rozdil hodnoty prvniho setu proti druhemu:", rozdil_cisel)
