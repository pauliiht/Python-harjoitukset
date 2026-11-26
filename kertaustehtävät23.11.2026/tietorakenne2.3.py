# Kirjoita funktio jossa käyttäjältä kysytään kurssi jonka osallistujamäärän haluaa tietää.
# Funktio laskee ja tulostaa ilmoittautuneiden määrän


#PÄÄTIETORAKENNE, 3 opiskelijaa ja kaikilla 3 kurssia
def ilmoittautuneet(sanakirja):
    kurssi = input("Minkä kurssin ilmoittautuneiden määrän haluat tarkistaa?")
    i = 0

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
        "kurssi1": "Musiikki",
        "kurssi2" : "Yritystalous",
        "kurssi3" : "Tuotannonohjaus"
    }
]
print(sanakirja)
      


