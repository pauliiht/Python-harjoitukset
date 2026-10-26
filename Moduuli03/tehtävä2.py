##Kirjoita ohjelma, joka kysyy laivan hyttiluokan (LUX, A, B, C)
##ja tulosta sanallisen kuvauksen luettelon mukaisesti käytä if/elif/else

hyttiluokka = input("Valitse hyttiluokkasi seuraavista: LUX, A, B tai C:")

if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella. ")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella. ")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella. ")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella. ")
else:
    print("Virheellinen hyttiluokka, tarkista valintasi.")