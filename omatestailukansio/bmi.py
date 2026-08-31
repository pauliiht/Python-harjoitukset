#Painoindeksi f kertoo että tulosteessa on käytetty muotoilua

pituus = float(input("Anna pituutesi: "))
paino = float(input("Anna painosi: "))

bmi = paino / (pituus / 100) **2

print(f"BMI:si on {bmi:10.2f}")

