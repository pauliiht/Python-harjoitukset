import math

def neliohinta(halkaisija, hinta):
    sade_metreina = (halkaisija / 100) / 2
    pinta_ala = math.pi * (sade_metreina ** 2)
    neliohinta = hinta/ pinta_ala
    return neliohinta

hinta = int(input("Kerro pizzan hinta: "))  
halkaisija = int(input("Kerro pizzan halkaisija: "))     

tulo = neliohinta(halkaisija, hinta)

print(f"Pizzan neliohinta on: {tulo:.2f} €/m2")
