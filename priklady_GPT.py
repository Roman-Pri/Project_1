# soucet zadanych cisel
prvni_zadane_cislo = int (input ("Zadej prvni cislo:"))
druhe_zadane_cislo = int (input ("Zadej druhe cislo:"))
print ("Soucet zadanych cisel je:", prvni_zadane_cislo + druhe_zadane_cislo)

# rozpoznani sudych a lichych cisel
zadane_cislo = int (input ("Zadej jakekoliv cele cislo:"))
if zadane_cislo % 2 == 0 :
    print  ("Zadane cislo", zadane_cislo, "je sude.")
else:
    print ("Zadane cislo", zadane_cislo, "je liche.")
    
