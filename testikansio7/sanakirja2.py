#Luo sanakirja joka sisältää eri hedelmien hinnat
#Kysy käyttäjältä hedelmän nimi ja tulosta sen hinta

hedelmat = {
     
        "ananas" : 5,
        "banaani" : 3,
        "omena" : 4
    }

hedelma = input("Minkä hedelmän hinnan haluat tietää? " )

if hedelma in hedelmat:
    print(hedelma, "hinta on", hedelmat[hedelma], "€/kpl")
else:
    print("Hedelmää ei löytynyt listalta.")
