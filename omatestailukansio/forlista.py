# Muistipaikka tyhjälle listalle:

nimet = []

# Pyydetään käyttäjältä nimiä:

nimi = input("Anna joku nimi: ")

while nimi != "":
    nimet.append(nimi)
    nimi = input("Anna joku nimi: ")

# tulosta kaikki annetut nimet:  
print (nimet)
 
# tervehtii kaikkia: 
for n in nimet:
    print(f"Tervehdys, {n}!")

# lopettaa ohjelman
print("Ohjelma loppui.")
