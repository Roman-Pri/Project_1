# Uvod
index = 0

while index < 5:
   print("index:", index)
   index = index + 1

print("Smyčka skončila")

# nepravdivy zapis
print(bool(5 < 5))

# ukazka smycka while s podminkou a log.operatorem and
index = 0
# kombinace podmínkového zápisu
# s logickým operátorem, kdy jeden je *False*
while index < 5 and index // 2 == 1:
   print("index:", index)
   index = index + 1

print("Smyčka skončila")

# ukazka smycka while s podminkou a log.operatorem or
index = 0
# kombinace podmínkového zápisu
# s logickým operátorem 
while index < 5 or index == 10:
   print("index:", index)
   index = index + 1

print("Smyčka skončila")

# ohlaseni break
index = 1

while index <= 6:
   print("index:", index)
   # Pokud je index 4 vypiš a ukonči smyčku 
   if index == 4:
       print("Mám hodnotu 4")
       break
   index = index + 1

# Ohlaseni continue
index = 0

while index <= 19:
   index = index + 1
   # pokud je aktuální hodnota proměnné sudá, 
   # pokračuj dále(přeskoč ji)
   if index % 2 == 0:
     continue
   print("index:", index)


# While & else
index = 0

while index < 5:
   print("index:", index)
   index = index + 1

print("Pokračuji..")

    # upraveno
index = 0

while index < 5:
   print("index:", index)
   index = index + 1

# vypíše se po ukončení smyčky
else:
   print("index:", index, "--> hodnoty jsou si rovny, ukončuji smyčku..")

print("Pokračuji..")

# while&else s break
index = 1

while index <= 6:
   print("index:", index)
   # --break-- přeskočí zbytek smyčky a i klauzuli else
   if index == 4:
       print("Mám hodnotu 4")
       break
   index = index + 1

else:
   print("index:", index, "--> hodnoty jsou si rovny, ukončuji smyčku..")

# interpret pokračuje až ZDE
print("Pokračuji..")

# nerizena nekonecna smycka

index = 1

while index > 0:
   print(index)
   index = index + 1   #vypnuti ctrl + C

#rizena nekonecna smycka

dotazovani = True

while dotazovani:
   odpoved = input("Zadej celé číslo od 1 do 5")

   if odpoved.isnumeric() and int(odpoved) in range(1, 6):
       print("Výborně")
       dotazovani = False
   else:
       print("Špatná hodnota, zkus to znovu")

#lepsi varianta s break (pozor neleze opakovat while s else)
while True:
   odpoved = input("Zadej celé číslo od 1 do 5")

   if odpoved.isnumeric() and int(odpoved) in range(1, 6):
       print("Výborně")
       break
   else:
       print("Špatná hodnota, zkus to znovu")


#ukoly v hodine
pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]

while pismena:
    print(pismena)
    pismeno = input("Vyhod pismeno:")
    if pismeno in pismena:
        print("Nasel jsi pismeno")
        pismena.remove(pismeno)
    else:
        print("Odstranil jsi pismena")

