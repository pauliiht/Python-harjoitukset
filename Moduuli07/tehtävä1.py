#Kirjoita ohjelma joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
#vuodenajan. Tallenna ohjelmassasi kk vastaavat vuodenajat merkkijonona monikkotietorakenteeseen.

kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
jarjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))

kuukausi = kuukaudet[jarjestysnumero - 1]

if jarjestysnumero in (12, 1, 2):
    print("Vuodenaika on talvi")
if jarjestysnumero in (3, 4, 5):
    print("Vuodenaika on kevät")
if jarjestysnumero in (6, 7, 8):
    print("Vuodenaika on kesä")
if jarjestysnumero in (9, 10, 11):
    print("Vuodenaika on syksy")
