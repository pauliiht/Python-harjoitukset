##oma tekele:
import random

def muokattunopanheitto(maksimiluku):
    nopanheitto = random.randint(1,maksimiluku)
    return nopanheitto
    
    
maksiminopanluku = int(input("Anna nopanluku: "))

while True:
    nopanheitto = muokattunopanheitto(maksiminopanluku)
    print(nopanheitto)
    if nopanheitto == maksiminopanluku:
        break
    
## OPEN VERSIO, TUTUSTU:

def noppa(suurin):
    luku = random.randit(1, suurin)
    return luku

tahkot = int(input("Kuinka isoa noppaa heitetään?"))
silmaluku = 0

while silmaluku != tahkot:
    silmaluku = noppa(tahkot)
    print("Heiton tulos oli", silmaluku)
    
    
