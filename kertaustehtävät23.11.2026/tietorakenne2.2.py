# Kysy käyttäjältä uusi oppilas kursseineen lisättäväksi sanakirjaan. Kysy kunnes syöttää tyhjän.
# Tulosta uudelleen koko sanakirja jotta näet että oppilas on lisätty
# Jää niin pienestä kiinni että saisin tehtyä, mutta kun ei niin ei. Saan vielä nimen lisättyä mutta en kursseja.


#PÄÄTIETORAKENNE, 3 opiskelijaa ja kaikilla 3 kurssia
sanakirja = [
    {
        "opiskelija" : "Pauliina",
        "kurssi1" : "Python",
        "kurssi2" : "Logistiikka",
        "kurssi3" : "Tuotannonohjaus"
    },
    {   "opiskelija" : "Matti",
        "kurssi1" : "Matematiikka",
        "kurssi2" : "Hankinta",
        "kurssi3" : "Fysiikka"
    },
     
    {  "opiskelija" : "Sini",
        "kurssi1" : "Musiikki",
        "kurssi2" : "Yritystalous",
        "kurssi3" : "Tuotannonohjaus"
    }
]

uusi = input("Kerro uuden opiskelijan nimi: ")
sanakirja.append(uusi)
while True:
    kurssi = input("Kerro millä kursseilla opiskelija on, tyhjä lopettaa: ")
    if kurssi == "":
        break
sanakirja.append(kurssi)

print(sanakirja)

