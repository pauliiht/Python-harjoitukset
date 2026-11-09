## OPEN VERSIO, oma ei ihan näin pitkälle päässyt!:
import math

def yksikkohinta(halkaisija, hinta):
    #pizzan pinta-ala
    sade = halkaisija/2
    ala = math.pi * (sade / 100) **2 ## muunnetaan sentit metreiksi
    #yksikköhinta
    return hinta / ala

halkaisija1 = float(input("Kerro ekan pizzan halkaisija (cm): "))  
hinta1 = int(input("Kerro ekan pizzan hinta: ")) 

halkaisija2 = int(input("Kerro tokan pizzan halkaisija (cm): "))   
hinta2 = int(input("Kerro tokan pizzan hinta: "))

pizza1 = yksikkohinta(halkaisija1, hinta1)
pizza2 = yksikkohinta(halkaisija2, hinta2)
print(f"Pizzan 1 yksikköhinta on {pizza1:.2f} €/nm")
print(f"Pizzan 2 yksikköhinta on {pizza2:.2f} €/nm")

if pizza1 < pizza2:
    print("Eka pizza on yksikköhinnalta halvempi.")
elif pizza2 < pizza1:
    print("Toka pizza on yksikköhinnalta halvempi.")
else:
    print("Yksikköhinta on sama.")