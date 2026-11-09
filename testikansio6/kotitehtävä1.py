## oma tekele:
import random

def nopanheitto():
    nopanheitto = random.randint(1,6)
    return nopanheitto

while True:
    heitto = nopanheitto()
    print(heitto)
    if heitto == 6:
        break
    
## OPEN VERSIO:

def noppa():
    luku = random.randit(1, 6)
    return luku

silmaluku = 0

while silmaluku != 6:
    silmaluku = noppa()
    print("Heiton tulos oli", silmaluku)
          
        