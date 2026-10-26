## Kirjoita ohjelma joka kysyy biologisen sukupuolen ja hemoglobiiniarvon
## Ohjelma ilmoittaa onko hemoglobiiniarvio matala, normaali vai korkea

sukupuoli = input("Kerro biologinen sukupuolesi: ")
HG = float(input("Kerro hemoglobiiniarvosi: "))

if sukupuoli == "nainen" and HG < 117:
    print("Hemoglobiiniarvosi on alhainen. ")
if sukupuoli == "nainen" and 117 <= HG <= 175:
    print("Hemoglobiiniarvosi on normaali. ")
if sukupuoli == "nainen" and HG > 175:
    print("Hemoglobiiniarvosi on korkea. ")

if sukupuoli == "mies" and HG < 134:
    print("Hemoglobiiniarvosi on alhainen. ")
if sukupuoli == "mies" and 134 <= HG <= 195:
    print("Hemoglobiiniarvosi on normaali. ")
if sukupuoli == "mies" and HG > 195:
    print("Hemoglobiiniarvosi on korkea. ")