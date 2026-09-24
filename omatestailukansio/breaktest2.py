## Toiston pysäyttäminen break komennolla

komento = input ("Anna komento: ")

while komento!="lopeta":
    if komento=="MAYDAY":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = input ("Anna komento: ")
    
print ("Toiminnot lopetettu.")

