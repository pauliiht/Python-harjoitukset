# Luo ohjelma, joka kysyy käyttäjälätä hänen lempivärinsä.
# Tarkista onko väri listalla, vastaa sen mukaisesti.

list = ["punainen", "valkoinen", "musta", "vihreä", "sininen", "keltainen"]

vari = input("Anna lempivärisi: ")

if vari in list:
    print ("Värisi löytyy listalta.")
else:
    print ("Väri ei löydy listalta.")
