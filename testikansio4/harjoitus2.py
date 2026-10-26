## Return ns tekee sen että tulos on käytettävissä myöhemminkin (rivi 11)

def neliosumma(eka, toka):
    ns = eka**2 + toka**2
    return ns

#PÄÄOHJELMA
luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Annan toinen luku: "))

tulos = neliosumma(luku1, luku2)

print(f"Lukujen neliosumma on: {tulos:.2f}")

