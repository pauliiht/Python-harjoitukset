# Kirjoita ohjelma joka kysyy suorakulmion kannan ja korkeuden. 
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

kanta = input("Anna suorakulmion kanta: ")
korkeus = input("Anna suorakulmion korkeus: ")

kanta = float(kanta)
korkeus = float(korkeus)


piiri = 2 * kanta + 2 * korkeus
pinta_ala = kanta * korkeus

print ("piiri:", piiri, "pinta_ala:", pinta_ala)


## float ja input voi laittaa samalle riville:
## kanta = float(input("Anna suorakulmion kanta: ")) jne


## print(f"Suorakulmion piiri on: {piiri}")
