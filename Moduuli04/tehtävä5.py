## Kirjoita ohjelma joka kysyy käyttäjätunnuksen ja salasaman. Jos jompikumpi tai molemmat on väärin, molemmat kysytään uudelleen
## Jatkuu kunnes oikein tai 5 kertaa väärin, tämän jälkeen...

tunnus = 12345
salasana = 0000

tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

while True:
    if tunnus=="12345" and salasana=="0000":
        break
    print ("Tervetuloa!")

    if tunnus !="12345" and salasana!="0000":
        continue
    print ("Annettu väärä käyttäjätunnus tai salasana, anna uudelleen: ")

