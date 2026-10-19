## Kirjoita ohjelma joka kysyy käyttäjältä kokonaisluvun. Jos luku on jaollinen kolmella,
## ohjelma tulostaa jaollinen kolmella, jaollinen viidellä ja jos molemmilla...

luku = int(input("Anna kokonaisluku: "))

if luku % 3 == 0 and luku % 5 == 0:
        print("jaollinen molemmilla luvuilla")

elif luku % 3 == 0:
    print("kolmella jaollinen")
        
elif luku % 5 == 0:
    print("viidellä jaollinen")
    