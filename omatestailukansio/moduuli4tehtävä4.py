# Tee ohjelma joka arpoo luvun 1-10 väliltä, peli arvuuttelee jne
# oikea ratkaisu joka käyty tunnilla läpi:

import random

luku = random.randint(1,10)

arvaus = int(input("Arvaa luku väliltä 1-10: "))

while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri arvaus!")
    else:
        print("Liian pieni arvaus!")
    arvaus = int(input("Arvaa luku väliltä 1-10: "))
   
print("Oikein arvattu!")
