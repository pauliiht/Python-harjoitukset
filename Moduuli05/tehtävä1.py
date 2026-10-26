import random

montanoppaa = int(input("Monta noppaa heitetään?: "))

summa = 0

for i in range(montanoppaa):
    noppa = random.randint(1, 6)
    summa = summa + noppa
    print("Heitto: ", i +1)
    print("Nopan silmäluku on: ",noppa)
    print("Nykyinen summa on: ",summa)

print("Heitettiin ", montanoppaa, " noppaa.")  
print("Lopullinen summa: ", summa)