# Laajenna ohjelmaa niin että käyttäjä voi antaa useita hedelmiä.
# Lasketaan yhteishinta ja ilmoitetaan jos hedelmää ei löydy. Lopetus tyhjällä syötteellä.

hedelmat = {
    "Omena" : 3,
    "Banaani" : 5,
    "Mango" : 8,
    "Vesimeloni" : 2
}

while True:
    hedelma = input("Minkä hedelmien hinnat haluat tietää? Tyhjä lopettaa kyselyn: ")
    if hedelma == "":
        break

if hedelma in hedelmat:
    print(hedelma, "hinta on", hedelmat[hedelma], "€/kpl")

else:
    print("Hedelmää ei löydy hinnastosta.")