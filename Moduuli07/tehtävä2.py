# Kirjoita ohjelma joka kysyy nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän.
# kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin: Uusi nimi tai Aiemmin syötetty nimi sen mukaan
# mukaan oliko se uusi vai jo aiemmin syötetty.Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
# allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen

nimet = set()

while True:
    nimi = input("Anna joku nimi, tyhjä merkkijono lopettaa.: ")
    if nimi == "":
        break
    
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        nimet.add(nimi)
        print("Uusi nimi")

for nimi in nimet:   
    print(nimi) 