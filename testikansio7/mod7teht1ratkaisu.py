#Kirjoita ohjelma joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
#vuodenajan. Tallenna ohjelmassasi kk vastaavat vuodenajat merkkijonona monikkotietorakenteeseen.
# Lähdin siis itse tekemään ihan eri tavalla, mutta tässä open malliesimerkki:

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä" "kesä", "syksy", "syksy", "syksy", "talvi")
kk = int(input("Anna kuukauden numero (1-12): "))

vuodenaika = vuodenajat[kk -1]

print("Vastaava vuodenaika on:", vuodenaika)