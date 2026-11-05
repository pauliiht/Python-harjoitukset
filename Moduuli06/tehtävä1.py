import random

def nopanheitto():
    nopanheitto = random.randint(1,6)
    return nopanheitto


while True:
    heitto = nopanheitto()
    print(heitto)
    if heitto == 6:
        break
     