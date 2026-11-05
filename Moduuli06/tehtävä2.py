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
