tuotteet = []
maarat = []

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? : "))
    tuotteet.append(tuote)
    maarat.append(maara)
    jatketaanko = input("Jatketaanko tuotantoa (kyllä/ei)? ")
    if jatketaanko == "ei":
        break
    
    print("Tuotanto lopetettu!")
    print("Valmistetut tuotteet: ")
    
    for i in range(len(tuotteet)):
        print(f"{tuotteet[i]}: {maarat[i]} kpl")
        
    