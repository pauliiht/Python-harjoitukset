# Kuten tehtävä 3, mutta muuta funktiota niin että se palauttaa suurimman yksttäisen päivän 
# tuotantomäärän. Laske suurin arvo silmukan avulla käyttämällä max()-funktiota

# FUNKTIO
def analysoi_tuotanto(tuotanto):
    return
   
tuotanto = [120, 150, 90, 180, 160]
kokonaismaara = sum(tuotanto)
keskiarvo = sum(tuotanto) / 5
suurin = max(tuotanto)

for t in tuotanto:
    print(f"Tuotanto yhteensä: {kokonaismaara} kpl")
    print(f"Keskimääräinen päivätuotanto: {keskiarvo}  kpl")
    print("Suurin tuotantomäärä per päivä oli: {max} kpl")

# Kokeilin muutamaa mutta en osannut tuota max-funktiota käyttää