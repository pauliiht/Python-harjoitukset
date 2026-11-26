# Kirjoita ohjelma joka laskee tuotteen valmistuksen kokonaiskustannukset.
# Luo funktio nimeltä laske_kustannus, joka saa parametreinä
# tuotteen valmistuskustannuksen kappaleelta ja valmistettavan määrän.

import math

#FUNKTIO
def laske_kustannus(kustannus, maara):
    lk = kustannus * maara
    return lk

#PÄÄOHJELMA   
kustannus = float(input("Anna tuotteen valmistuskustannus (€): "))
maara = int(input("Kuinka monta tuotetta valmistetaan? "))

tulos = laske_kustannus(kustannus, maara)

print(f"Valmistuksen kokonaiskustannus on:  {tulos:.2f} €")
