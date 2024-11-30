cislo= int (input ("zadej cislo: "))
if cislo % 3 == 0 and cislo % 5 == 0:
    print ("fizzBuzz")
elif cislo % 3 == 0:
    print ("fizz")
elif cislo % 5 == 0:
    print ("Buzz")
else:
    print ("spatne",cislo)



cislo_1= float(input("zadejte prvni cislo:"))
cislo_2= float(input("zadejte druhe cislo:"))
if cislo_1 == cislo_2:
    print ("obe cisla jsou stejna.")
else:
    if cislo_1 < cislo_2:
        print ("Prvni cislo je mensi nez druhe.")
    else:
        print ("Prvni cislo je vetsi nez druhe.")