# Kirjoita ohjelma joka analysoi tehtaan päivittäisiä tuotantomääriä.
# Ohjelmassa on valmiina lista, joka sisältää viiden päivän tuotantomäärät.
# Luo funktio analysoi_tuotanto, joka saa parametrinä listan tuotantomääristä.
# Funktio laskee for-silmukan avulla kaikkien päivien tuotantomäärät yhteen ja palauttaa kokonaismäärän.
# Pääohjelma kutsuu funktiota ja tulostaa tuotantomäärän kokonaismäärän ja keskimääräisen päivätuotannon.

# FUNKTIO
def analysoi_tuotanto(tuotanto):
    return
   
tuotanto = [120, 150, 90, 180, 160]
kokonaismaara = sum(tuotanto)
keskiarvo = sum(tuotanto) / 5

for t in tuotanto:
    print(f"Tuotanto yhteensä: {kokonaismaara} kpl")
    print(f"Keskimääräinen päivätuotanto: {keskiarvo}  kpl")

# Tulostaa luvut nyt 5 krt alkioiden määrän mukaan, mutta en keksi mitä pitäisi muuttaa jotta tulisi vaan kerran.
# Pitäisikö funktiossa olla tuo lista tai muita tietoja, mitä?