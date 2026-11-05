import math

def litrat(gallonat):
    laskukaava = 3.785
    tulo = gallonat * laskukaava
    return tulo

while True:
    polttoaine = int(input("Anna polttoaineen määrä gallonoina, negatiivinen luku lopettaa ohjelman: "))
    
    if polttoaine <0:
        print("Ohjelma päättyy negatiivisen luvun takia.")
        break
     
    tulos = litrat(polttoaine)
    print(f"Antamasi gallonamäärä on {tulos} litraa.")