#Parametrit on tietoa joka lähetetään funktiolle
#Määritetään jokaisen funktiokutsun yhteydessä, parametrille annettava arvo
#Määritettävä kuinka monta kertaa funktio toistetaan

def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hyvää päivää " + str(i+1) + ". kerran.")
       # print(f"Hyvää päivää {i+1}. kerran.") toinen tapa kirjoittaa edellinen rivi
    return

#PÄÄOHJELMA

print("Testataan tervehdys-funktiota:")
tervehdi(3)
print("Testataan vielä toisen kerran että toimii...")
tervehdi(5)