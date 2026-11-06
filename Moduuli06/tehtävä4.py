def summa(numerolista):
    tulos = 0
    for luku in numerolista:
        tulos += luku
    return tulos
    
lista = [1, 3, 5, 7, 9]
tulos = summa(lista)

print(f"Lukujen summa on: {tulos}")

