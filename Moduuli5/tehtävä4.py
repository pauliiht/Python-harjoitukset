
kaupunkilista = []

kaupunki = input("Anna kaupunki 1/5: ")

while kaupunki !="":
    kaupunkilista.append(kaupunki)
    kaupunki = input("Anna kaupunki 2/5: ")
    kaupunkilista.append(kaupunki)
    kaupunki = input("Anna kaupunki 3/5: ")
    kaupunkilista.append(kaupunki)
    kaupunki = input("Anna kaupunki 4/5: ")
    kaupunkilista.append(kaupunki)
    kaupunki = input("Anna kaupunki 5/5: ")
    kaupunkilista.append(kaupunki)
    break

for kaupunki in kaupunkilista:
    print(kaupunki)