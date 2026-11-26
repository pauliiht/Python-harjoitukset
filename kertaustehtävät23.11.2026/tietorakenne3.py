#Kirjoita ohjelma joka ylläpitää tehtaan varastotietoja sanakirjan avulla.
#Ohjelmassain valmis sanakirja jossa avain on tuotteen nimi ja arvo varastoäärä

varasto = [
    {
        "tuote" : "Pöytä",
        "maara" : "20"
    },
    {
        "tuote" : "Tuoli",
        "maara" : "50"
    },
    {   "tuote" : "Hylly",
        "maara" : "15"
    }
]

for t in varasto:
    print(f"tuote","maara")