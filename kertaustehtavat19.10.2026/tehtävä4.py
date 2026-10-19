## Kirjoita ohjelma joka kysyy kokonaislukuja. Jos luku on pienempi kuin 0, tulosta "virheellinen numero"
## Jos luku on suurempi kuin 0, tulosta luvun  neliöjuuri Python sqrt. Molempien jälkeen kysyy uutta lukua, 0 lopettaa

import math

while True:
    luku = int(input("Anna joku kokonaisluku: "))
    
    if luku == 0:
        break
    elif luku < 0:
        print("Virheellinen luku.")
    else:
        print(f"{math.sqrt(luku):.4f}")
        
        
    

