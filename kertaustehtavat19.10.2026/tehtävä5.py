## Kirjoita ohjelma joka pyytää käyttäjältä sanoka. Jos kirjoittaa "loppu, ohjelma tulostaa ja lopettaa

satu = []

sana = input("Anna joku sana: ")

while sana != "":
    satu.append(sana)
    sana = input("Anna joku sana: ")
    
    if sana == "loppu":
        print("Ohjelma loppui.")
        break

tuloste = " " .join(satu)
print(tuloste)

## En keksinyt miten saada silmukka lppumaan jos syöttää saman sanan
