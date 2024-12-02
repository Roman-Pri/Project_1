print ("indexovani" [:5])
print ("indexovani" [-5:])
print ("indexovani" [::3])



kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

kg_vysledek = kg_pocet * kg_lb
km_vysledek = km_pocet * km_mile
l_vysledek = l_pocet * l_gal

print (km_pocet, "km je rovno", km_vysledek, "mil")
print (kg_pocet, "kg je rovno", kg_vysledek, "lb")
print (l_pocet, "l je rovno", l_vysledek, "gal")


mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000
cena_merc_rolls = mercedes + rolls_royce
cena_2_rolls = 2*(rolls_royce + vybava)
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc
cena_2_merc = 2 * mercedes

print ("Cena za mercedes a rolss royce:", cena_merc_rolls)
print ("Cena za 2 rolls royce s priplatkovou vybavou", cena_2_rolls)
print ("Cena za mercedes s priplatkovou vybavou", cena_merc_s_vybavou)
print ("Cena za mercedes po sleve:", merc_se_slevou)
print ("Cena za dva mercedesy:", cena_2_merc)


jmeno = "Lukas"
prijmeni = "Dvorak"
cele_jmeno = jmeno + " " + prijmeni
delka_jmena = len (cele_jmeno)
print("delka jmena:", delka_jmena)
print ("=" * delka_jmena)
print (cele_jmeno)
print ("=" * delka_jmena)
