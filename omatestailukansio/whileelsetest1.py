## WHILE / ELSE rakenne, voidaan käyttää kuten IF. ELSE ajetaan kun alkuehdosta tulee epätosi

komento = input ("Anna komento: ")

while komento!="lopeta":
    if komento=="MAYDAY":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print ("Näkemiin.")
    
print ("Toiminnot lopetettu. ")


