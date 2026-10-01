## WHILE TRUE jos while lauseke on alusta asti TRUE. muista asettaa päättymisehto tai lopetuskäsky

coffee = 5
coins_given = 0

while True:
    coins_given += 1
    print("Coins given:", coins_given)
    
    if coins_given == coffee:
        break
    
print("Coffee is paid.")

