def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat: ")
    for t in tavarat:
        print(" - " + t)
    

reppu = ["kartta", "juomapullo", "kompassi"]
inventaario(reppu)
reppu.append("sampyla")
inventaario(reppu)
