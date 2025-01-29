jmeno_souboru = "novy_soubor.txt"
pozdrav = "Ahoj, toto je první zápis do textového souboru"

# otevreni souboru
txt_soubor = open(jmeno_souboru, mode="w")

# zapis do souboru
txt_soubor.write(pozdrav)

# řádné zavření souboru
txt_soubor.close()


# cteni souboru
txt_soubor = open("novy_soubor.txt", mode="r")
obsah_txt = txt_soubor.read()
print(obsah_txt)
txt_soubor.close()

# cteni a nahrani dalsiho radku - r+
druhy_radek = " Ted pridavas druhy radek"

txt_soubor = open("novy_soubor.txt", mode="r+")
obsah_txt = txt_soubor.read()
txt_soubor.write(druhy_radek)

txt_soubor.close()

# vyhnuti nezadoucimu prepisu - mode = "a"
treti_radek = "Toto je treti radek tveho puvodniho souboru souboru ^.^"

txt_soubor = open("novy_soubor.txt", mode="a")
txt_soubor.write(treti_radek)
txt_soubor.close()
