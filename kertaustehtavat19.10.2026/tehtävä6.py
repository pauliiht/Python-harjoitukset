## Kirjoita ohjelma, joka pyytää käyttäjältä arvoja ja lisää ne listaan
## Jokaisen lisäyksen jälkeen tulostus kahdella tavalla;
## lisäysjärjestyksessä ja pienimmästä suurimpaan. loppuu kun 0

lista = []

while True:
    luku = int(input("Kerro joku luku, numero 0 lopettaa tehtävän: "))
    
    if luku == 0:
        break
    lista.append(luku)
    
    print("Lisäysjärjestyksessä luvut ovat:" , lista)
    
    print("Luvut pienimmästä suurimpaan:", sorted(lista))
    
