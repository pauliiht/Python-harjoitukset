## Kirjoita ohjelma, joka kysyy lukuja siihen saakka kunnes syöttää tyhjän merkkijonon lopetusmerkiksi.
## Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman!

import math

while True:
    luku = int(input("Anna joku luku, tyhjä välilyönti lopettaa tehtävän: "))
    if luku:
        continue
    if luku == " ":
        break
     
    