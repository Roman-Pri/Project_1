# nahrani knihovny a pouziti modulu floor(zaokrouhlovani dolu na cele cislo)
import math
print(dir(math))
print(math.floor(2.56))

#import<knihovna>
import math
print(math.pi)

#from<knihovna>import*
from sys import *
from math import *

print(
# odkud pochází proměnná 'e'? sys/math?...
	e,           
	version, sep="\n"
)
#from <knihovna> import <objekt,promenna>
from math import e

print(e)

#nebo dve promenne z jedne knihovny
from math import e, pi #spojeni carkou a zapis za sebe

print(e)
print(pi)

#from <knihovna>import<objekt>as<alias>
from math import pi as p

print(p)

#import<knihovna>as<alias>
import math as m

print(m.pi)

#skript i knihovna
import pomocna

print(pomocna)

print(pomocna.var_2)

#moduly
# modul pro práci s operačním systémem
import os  
  
# modul pro přístup k některým systémovým proměnným 
import sys

# modul pro práci s pseudo-náhodnými procesy    
import random  

print(
    "os" in dir() \
    and "sys" in dir() \
    and "random" in dir()
)
print("muj_modul" in dir())


#doplneni z lekce - kdyz modul neni ve slozce(v balicku)
import zkouska.mesta #jdeme do slozky zkouska a do souboru mesta