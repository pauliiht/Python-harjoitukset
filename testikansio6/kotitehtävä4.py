## oma tekele:

def summa(numerolista):
    tulos = 0
    for luku in numerolista:
        tulos += luku
    return tulos
    
lista = [1, 3, 5, 7, 9]
tulos = summa(lista)

print(f"Lukujen summa on: {tulos}")

## OPEN VERSIO:
def summa(l):
    _summa = 0
    for luku in l:
        _summa += luku
    return _summa
        
luvut = [8, 12, 3, 565, 91]
print("Lista:", luvut)

tulos = summa(luvut)
print("Lukujen summa on:", tulos)

