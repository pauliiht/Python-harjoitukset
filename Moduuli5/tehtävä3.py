## Alkuluku: Suurempi kuin 1 ja luku joka jaollinen 1 ja itsellään
# 2 ainoa parillinen alkuluku

import math

## Kysytään kokonaislukua

luku = int(input("Anna kokonaisluku: "))

## Tarkistetaan onko annettu kokonaisluku alkuluku
## Kerrotaan käyttäjälle onko annettu kokonaisluku alkuluku

if luku <= 1:
    print(f"Luku {luku} ei ole alkuluku.")

if luku == 2:
    print(f"Luku {luku} on alkuluku.")
    
if luku % 2 == 0:
    print(f"Luku {luku} ei ole alkuluku.")
    
juuri = int(math.sqrt(luku)) + 1
for luku in range(3, juuri, 2):
    if luku % luku == 0:
        print(f"Luku {luku} ei ole alkuluku.")

else:
    print(f"Luku {luku} on alkuluku.")