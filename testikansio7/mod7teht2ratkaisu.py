# Kirjoita ohjelma joka kysyy nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän.
# kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin: Uusi nimi tai Aiemmin syötetty nimi sen mukaan
# mukaan oliko se uusi vai jo aiemmin syötetty.Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
# allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen
# Ja tässä malliesimerkki, oma oli suht lähellä tätä:

nimet = set()

nimi = input("Anna nimi, tyhjä lopettaa: ")

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi!")
    else:
        print("Uusi nimi!")
        nimet.add(nimi)
        
    nimi = input("Anna nimi, tyhjä lopettaa: ")

print("Syötetyt nimet: ")
for n in nimet:
    print(n)
    
    