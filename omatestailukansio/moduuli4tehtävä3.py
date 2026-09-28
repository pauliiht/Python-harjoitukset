# Tee ohjelma joka kysyy lukuja, lopuksi listaa pienimmän ja suurimman:
# oikea ratkaisu joka käyty tunnilla läpi:

luku = input("Anna kokonaisluku, tyhjä lopettaa: ")

pieni = luku
suuri = luku

while luku != " ":
    numero = int(luku)
    
    #Vertaillaan onko pienempi tai isompi
    
    if pieni == luku or numero < pieni:
        pieni = numero
    
    if suuri == luku or numero > suuri:
        suuri = numero
        
    luku = input("Anna kokonaisluku, tyhjä lopettaa: ")
    
print("Pienin luku on", pieni)
print("Suurin luku on", suuri)