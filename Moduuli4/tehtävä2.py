## Kirjoita ohjelma joka muuntaa tuumia senttimetreiksi kunnes antaa negatiivisen tuumamäärän

import math

## tuuma = 2.54 cm

while True:
    number = float(input("Anna tuumaluku: "))
    if number <= -1:
        break
    if number >= 1:
        print (f"Pituus senttimetreinä on {number * 2.54}")
           
           