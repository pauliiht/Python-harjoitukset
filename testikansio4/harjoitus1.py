## Kirjoita funktio nimeltä keskiarvo, joka saa kolme kokonaislukuarvoa argumentteina.
## Funktio tulostaa näiden 3 luvun arimeettinen keskiarvo
## Kysy luvut käyttäjätä input-funktion avulla

def keskiarvo(luku1, luku2, luku3):
    tulos = (luku1 + luku2 + luku3) / 3
    print("Aritmeettinen keskiarvo on: ", tulos)
    return

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Annan toinen luku: "))
luku3 = float(input("Annan kolmas luku: "))

keskiarvo(luku1, luku2, luku3)

