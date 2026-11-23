#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
#Ohjelma kysyy käyttäjältä haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa
#Jos valitsee uuden, ohjelma kysyy ICAO koodin ja tulostaa sitä vastaavan lentoaseman nimen. jne
# En päässy kauas, tässä malliesimerkki. ICAO-koodi on avain

lentoasemat = {
    "EFHK": "HelsinkiVantaa",
    "EFRO" : "Rovaniemi",
    "EFOU" : "Oulu",
    }
 
while True:
    print("Valitse toiminto: A = syötä, B = hae, Q = lopeta ")
    
    valinta = input("Mitä haluat tehdä: ").upper()
    
    if valinta == "A":
        icao = input("Anna uuden lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna uuden lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    elif valinta == "B":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Koodilla ei löydy nimeä.")
    elif valinta == "Q":
        print("Ohjelma päättyy...")
        break
    
    