## Kirjoita ohjelma joka simuloi tuotantolinjan toimintaa.
## Ohjelma tulostaa: Tuote valmistettu ja kysyy "jatketaanko tuotantoa", jatkuu kunnes EI
komento = ""

while True:
    print("Tuote valmistettu.")
    komento = input("Jatketaanko tuotantoa?")
    if komento == "Ei":
        print("Tuotanto lopetettu.")
        break
    
    