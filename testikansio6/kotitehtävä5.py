## oma versio:
def parilliset(numerolista):
    tulos = []
    for luku in numerolista:
        if luku % 2 == 0:
            tulos.append(luku)       
    return tulos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
karsittu_lista = parilliset(lista)

print("Alkuperäinen lista:", lista)
print("Karsittu lista:", karsittu_lista)

## OPEN VERSIO:

def parilliset(l):
    uusi_lista = []
    for luku in l:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
luvut2 = parilliset(luvut)

print("Alkuperäinen lista:", luvut)
print("Parillisten lukujen lista;", luvut2)

