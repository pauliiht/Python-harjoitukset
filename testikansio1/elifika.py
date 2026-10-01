## ikäluokat if ja elif voi olla useita, mutta vain yksi voi olla totta. jos mikään ei
## ole totta, tulee else komento

ika = int(input("Anna ikäsi: "))

if ika >= 65:
    print("Olet eläkkeellä.")
elif ika >= 18:
    print ("Olet työikäinen.")
elif ika >= 7:
    print ("olet kouikäinen.")
else:
    print ("Olet pieni lapsi.")
    
