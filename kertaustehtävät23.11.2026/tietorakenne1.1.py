# Luo sanakirja joka sisältää eri hedelmien hinnat.
# Kysy käyttäjältä hedelmän nimi ja tulosta hinta

hedelmat = {
    "Omena" : 3,
    "Banaani" : 5,
    "Mango" : 8,
    "Vesimeloni" : 2
}

hedelma = input("Minkä hedelmän hinnan haluat? ")

if hedelma in hedelmat:
    print(hedelma, "hinta on", hedelmat[hedelma], "€/kpl")