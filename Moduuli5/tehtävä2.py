# lopuksi halutaan lista

lista = []

while True:
    kysykayttajalta = input("Kerro joku luku, tyhjä merkkijono lopettaa tehtävän: ")
    if kysykayttajalta == "":
        break
    int(kysykayttajalta)
    lista.append(kysykayttajalta)

lista.sort(reverse=True)

for alkio in range(5):
    print(lista [alkio])