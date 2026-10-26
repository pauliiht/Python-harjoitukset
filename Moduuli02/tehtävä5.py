# Kirjoita ohjelma joka kysyy massan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kg ja g ja ilmoittaa tuloksen käyttäjälle.

import math

leiviskat= float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti_g = 13.3
naula_g = 32 * luoti_g
leiviska_g = 20 * naula_g

kokonaismassa_g = (leiviskat * leiviska_g) + (naulat * naula_g) + (luodit * luoti_g)

kilogrammat = int(kokonaismassa_g // 1000)
grammat = kokonaismassa_g % 1000

print (f"Tulos on {kilogrammat} kg ja {grammat:.2f} g.")

