## Kirjoita ohjelma joka kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän.
## Ohjelma tulostaa päiväpalkan

tuntipalkka = int(input("Mikä on tuntipalkkasi: "))
tunnit = int(input("Kerro monta tuntia teit töitä: "))
paiva = input("Mikä oli viikonpäivä jolloin työskentelit: ")

if paiva == "sunnuntai":
    palkka = 2 * tuntipalkka * tunnit
    print(f"Sait palkkaa: {palkka} €")
    
else:
    palkka = tuntipalkka * tunnit
    print(f"Sait palkkaa: {palkka} €")

