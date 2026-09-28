##Tee ohjelma joka listaa kolmella jaolliset luvut välillä 1-1000:
## oikea ratkaisu joka käyty tunnilla läpi, varmaan parempi tuo tolla %-merkillä
## Itse tein ihan toisin!

luku = 1

while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1
