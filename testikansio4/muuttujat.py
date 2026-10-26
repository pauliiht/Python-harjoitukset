## Muuttujat

def vaihda ():
    _kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + _kaupunki)
    return

#PÄÄOHJELMA

kaupunki = "Helsinki"
print("Kaupungin nimi alunperin: " + kaupunki)
vaihda()
print("Globaalin kaupungin nimi: " + kaupunki)

