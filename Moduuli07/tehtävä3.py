#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
#Ohjelma kysyy käyttäjältä haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa
#Jos valitsee uuden, ohjelma kysyy ICAO koodin ja tulostaa sitä vastaavan lentoaseman nimen. jne
#Mistä tätä oikein lähtee purkamaan??? 

kentat = {"HelsinkiVantaa": "EFHK",
          "Rovaniemi": "EFRO",
          "Oulu": "EFOU",
          "Turku": "EFTU",
          "Ivalo": "EFIV",
          "Vaasa": "EFVA"
        }
 
while True:
    komento = input("Valitse haluamasi vaihtoehto: A: syöttää uuden lentoaseman, B: hakea jo syötetyn lentoaseman tiedot vai C: lopettaa haun: ")
        if komento == "A":
            icao = input("Anna lentoaseman ICAO-koodi: ")
            kentta = input("Anna lentoaseman nimi: ")
    print("Lentokentän tiedot: {}")
        
    if komento == "B":
        print("Anna lentoaseman ICAO-koodi.")
        print("Lentokentän tiedot: {}")
        
    if komento == "C":
        print("Haku päättyy.")
        