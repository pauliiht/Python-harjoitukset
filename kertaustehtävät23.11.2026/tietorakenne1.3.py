# Jos syötetään hedelmä jota ei löysy hinnastosta, ohjelma kysyy haluaako käyttäjä lisätä sen ja antaa hinnan.
# Lopuksi ohjelma tulostaa päivitetyn hinnaston.

hedelmat = {
    "Omena" : 3,
    "Banaani" : 5,
    "Mango" : 8,
    "Vesimeloni" : 2
}

hedelma = input("Minkä hedelmän hinnan haluat? ")
if hedelma in hedelmat:
    print(hedelma, "hinta on", hedelmat[hedelma], "€/kpl")
    
if hedelma not in hedelmat:
    input("Lisätäänkö uusi hedelmä hinnastoon, vastaa YES tai NO ")
    if == "YES":
        input("Anna uuden hedelmän nimi: ")
        int(input("Anna hedelmän hinta "))
    hedelmat.append
    print(hedelmat)

    