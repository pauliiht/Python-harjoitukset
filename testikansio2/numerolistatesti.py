numerot = []

num = int(input("Anna numero listaan: "))

while num != 0:
    numerot.append(num)
    num= int(input("Anna numero listaan: "))
 
print(numerot)   
summa = 0   
    
for numero in numerot:
    summa += numero
    print("Summa nyt: ", summa)
    
print("Lopullinen summa on:", summa)


    