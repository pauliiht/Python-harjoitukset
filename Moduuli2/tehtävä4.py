# Kirjoita ohjelma joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

kokonaisluku1 = input ("Anna ensimmäinen kokonaisluku: ")
kokonaisluku2 = input ("Anna toinen kokonaisluku: ")
kokonaisluku3 = input ("Anna kolmas kokonaisluku: ")

kokonaisluku1 = int(kokonaisluku1)
kokonaisluku2 = int(kokonaisluku2)
kokonaisluku3 = int(kokonaisluku3)

summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
keskiarvo = summa / 3

print ("Lukujen summa on", summa)
print ("Lukujen tulo on", tulo)
print ("Lukujen keskiarvo on", keskiarvo)