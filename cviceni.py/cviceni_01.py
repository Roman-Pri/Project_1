# cviceni c.1 priklad indexovani
# Prvních 5 písmen slova 'indexování',
# posledních 5 písmen slova 'indexování',
# každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i"),
# všechny výstupy zapiš přímo do funkce print,výstup dále úprav podle ukázky níže.
print("Prvnich 5 pismen")
print("indexovani"[:5])
print("Poslednich 5 pismen")
print("indexovani"[-5:])
print("Kazde 3 pismeno slova (pocinaje prvnim)")
print("indexovani"[::3])


# cviceni c.1 priklad prevod jednotek
# Převod z kilogramů na libry,z kilometrů na míle,z litrů na galony.
# prevodni hodnoty
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26
# mnozstvi
kg_pocet = 80
km_pocet = 54
l_pocet = 5
# vypocet
kg_vysledek = float(kg_lb*kg_pocet)
km_vysledek = float(km_mile*km_pocet)
li_vysledek = float(l_gal*l_pocet)
# vypis
print (kg_pocet, "kg je", kg_vysledek, "lb")
print (km_pocet, "km je", km_vysledek, "mil")
print (l_pocet, "l je", li_vysledek, "gal")


# cviceni c.1 operace ze stringy inteegery
# cenik
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
# sleva
sleva_merc = 5000
# vypocty
cena_2_merc = mercedes * 2
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = (rolls_royce + vybava) * 2
cena_merc_s_vybavou = mercedes + vybava
cena_merc_po_sleve = mercedes - sleva_merc
# vypis
print (cena_2_merc)
print (cena_merc_a_rolls)
print (cena_2_rolls_s_vybavou)
print (cena_merc_s_vybavou)
print (cena_merc_po_sleve)


# cviceni c.1 seznam
# udaje
jmeno = "Lukáš"
prijmeni = "Dvořák"

# slouceni a delka
cele_jmeno = jmeno + " " + prijmeni
print (cele_jmeno)
print ("Délka jména je:", len(cele_jmeno))
# ohraniceni
print ("=" * len (cele_jmeno))
print (cele_jmeno)
print ("=" * len (cele_jmeno))
