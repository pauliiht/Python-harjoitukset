## muistutus että if lausekkeen ohessa ei oo pakko olla else-lauseketta


ika = int(input("Anna ikäsi: "))

if ika == 18:
    print("Olet täysi-ikäinen")
elif ika > 18:
    print("Olen yli 18 vuotta")
elif ika < 18:
    print("Olet alaikäinen")
    
