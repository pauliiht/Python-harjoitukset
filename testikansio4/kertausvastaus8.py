## tää oli ihan oikein: ainoo mitä vaihdoin oli tuo for jälkeen pelkkä k 
## tähän tosiaan riittää pelkkä kirjain, joka viittaa listaan

lista = [12.50, 8.20, 15.0, 6.5, 10.8] 

kokonaiskustannus = 0

print("Yksittäiset valmistuskustannukset:")

for k in lista:
    print(f"Tuotteen valmistuskustannus: {k} €")
    kokonaiskustannus += k
    
print(f"Valmistuskustannukset ovat yhteensä {kokonaiskustannus:.2f} €")