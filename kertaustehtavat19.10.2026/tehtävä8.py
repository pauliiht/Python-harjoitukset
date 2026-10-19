## Kirjoita ohjelma, jossa on lista viiden tuotteen valmistuskustannuksista.
## Ohjelma käy kustannukset läpi for-silmukan avulla ja tulostaa sen.
## Samalla ohjelma laskee kaikkien tuotteiden kustannukset yhteensä.
## Lopuksi ohjelma tulostaa kokonauskustannuksen

lista = [12.50, 8.20, 15.0, 6.5, 10.8] 

kokonaiskustannus = 0  

print("Yksittäiset valmistuskustannukset:")

for hinta in lista:
    print(f"Tuotteen valmistuskustannus: {hinta} €")
    kokonaiskustannus += hinta
    
print(f"Valmistuskustannukset ovat yhteensä {kokonaiskustannus:.2f} €")
