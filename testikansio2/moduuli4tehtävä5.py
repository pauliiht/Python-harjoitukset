# Tee ohjelma joka kysyy käyttis ja salasana

salasana = "qwerty"
käyttäjätunnus = "omanimi"

yritykset = 0
yht = 5

print("Tervetuloa kokeilemaan käyttis ja salasana, yrityksiä on 5 kpl")

while True:
    yritykset += 1
    kyritys = input("anna käyttäjätunnus: ")
    syritys = input("anna salasanasi: ")
    
    if yritykset == yht:
        print("pääsy evätty")
        break
    
    if salasana != syritys or käyttäjätunnus != kyritys:
        print("väärin")
        continue
    
    if salasana == syritys and käyttäjätunnus == kyritys:
        print("Tervetuloa!")
        break
    
tunnus = "pauliina"
salasana = "kissa"

while yritykset < 5:
    tunnus = input("Anna tunnus: ")
    salasana = input ("Anna salasana: ")
    
    if tunnus == "pauliina" ans salasana == "kissa":
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana!")
        yritykset += 1
        
    
    
    
    
