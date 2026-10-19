## Kirjoita ohjelma joka simuloi tehtaan tuotantoa.
## Ohjelma kysyy mitä tuotetta valmistetaan ja kuinka monta
## Tallenna tuotteiden nimet ja määrä omiin listoihinsa
## Kysy: jatketaanko tuotantoa jos kyllä, jatka, jos ei lopetus
## Lopuksi ohjelma tulostaan kaikki valmistetut tuotteet ja määrät

tuotteet = []
maara = []

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    
    tuotteet.append(tuote)
    maara.append(maara)
    
    if tuote == "Ei":
        break
    if tuote == "Kyllä":
         maara = int(input("Kuinka monta valmistetaan?"))
         maara.append(maara)         

print(list tuote ja maara)
      