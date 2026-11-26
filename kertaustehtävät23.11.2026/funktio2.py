# Kirjoita ohjelma joka laskee tuotteen myynnistä saatavan voiton.
# Luo funktio laske_voitto, joka saa parametreina tuotteen
# valmistuskustannuksen, myyntihinnan ja myytyjen tuotteiden määrän.

import math

#FUNKTIO
def laske_voitto(myyntihinta, valmistuskustannus, maara):
    lv = (myyntihinta - valmistuskustannus) * maara
    return lv

# PÄÄOHJELMA

myyntihinta = float(input("Anna tuotteen myyntihinta (€): "))
valmistuskustannus = float(input("Anna tuotteen valmistuskustannus (€): "))
maara = int(input("Kuinka monta tuotetta valmistetaan? "))

tulos = laske_voitto(myyntihinta, valmistuskustannus, maara)

if tulos < 0 :
    print(f"Kokonaisvoitto on:  {tulos:.2f} €")
    print("Tuotanto on tappiollista!")
    
else:
    print(f"Kokonaisvoitto on:  {tulos:.2f} €")
    print("Tuotanto on kannattavaa!") 