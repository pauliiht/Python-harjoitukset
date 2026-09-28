# Luo ostoslista ostettavista tuotteista.

list = ["maito", "leipä", "voi", "juusto", "banaani"]

while list:
    tuote = input("Anna ostamasi tuote: ")
    if tuote in list:
        list.remove("tuote")
    print(list)
    tuote = input("Anna ostamasi tuote: ")
else:
    print("Tuote ei ole listalla.")

