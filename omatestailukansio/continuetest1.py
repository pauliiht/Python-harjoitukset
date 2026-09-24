## CONTINUE-lauseke, sallii poikkeuksen toistorakenteen sisällä sitä pysäyttämättä

sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    if number >= 10:
        continue
    sum += number

print (f"The sum is {sum}")

