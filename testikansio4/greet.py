## tässä jälkimmäinen funktio kutsuu ekaa funktiota

def tervehdi(nimi):
    print("Moikka, " + nimi)
    return

def tervehdi_monesti(_nimi, kerrat):
    while kerrat > 0:
        tervehdi(_nimi)
        kerrat -= 1
    return

#PÄÄOHJELMA

tervehdi_monesti("Heidi", 3)
