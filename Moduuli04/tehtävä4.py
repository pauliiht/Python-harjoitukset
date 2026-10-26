## Kirjoita peli, jossa tietokone arpoo kokonaisluvun 1-10. Kone arvuuttelee lukua pelaajata siihen asti,
## kunnes arvaa oikein. Kunkin arvauksen jälkeen tulostaa jonkin lausekkeen...

import random

arvottu_luku = random.randint(1, 10)

while True:
    number = int(input("Arvaa kokonaisluku väliltä 1-10: "))
    
    if number == arvottu_luku:
        break
    print ("Oikein!")
    
    if number < arvottu_luku:
        continue
    print ("Liian pieni arvaus, arvaa uudelleen.")
    
    if number > arvottu_luku:
        continue
    print ("Liian suuri arvaus, arvaa uudelleen.")
    
    
