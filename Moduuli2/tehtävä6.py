# Kirjoita ohjelma joka arpoo ja tulostaa kaksi erilaista numerolukon koodia.
# kolmenumeroinen koodi, jonka kukin numeromerkki on väliltä 0-9.
# Nelinumeroinen koodi, jonka kukin numeromerkki on välillä 1-6.

## ei onnistunut itse ollenkaan, katsottu tunnilla ratkaisu ja kopsattu tähän:


import random


num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)

print (f"Koodi on: {num1}{num2}{num3}")


num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
num3 = random.randint(1, 6)
num4 = random.randint(1, 6)

print (f"Koodi on: {num1}{num2}{num3}{num4}")


