## oma tekele:
def litrat(gallonat):
    laskukaava = 3.785
    tulo = gallonat * laskukaava
    return tulo

while True:
    polttoaine = int(input("Anna polttoaineen määrä gallonoina, negatiivinen luku lopettaa ohjelman: "))
    
    if polttoaine <0:
        print("Ohjelma päättyy negatiivisen luvun takia.")
        break
     
    tulos = litrat(polttoaine)
    print(f"Antamasi gallonamäärä on {tulos} litraa.")

## OPEN VERSIO:
def litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

g = float(input("Anna gallonamäärä jonka haluat muuntaa liroiksi (neg lopettaa): "))
while g >= 0:
    l = litroiksi(g)
    print("Määrä litroina on:", l)
    g = float(input("Anna gallonamäärä jonka haluat muuntaa liroiksi (neg lopettaa): "))
    
print("Lopetaan ohjelma...")
 