# PÄÄTIETORAKENNE = jonka alla 3 sanakirjaa, kullakin autolla oma

autot = [
    {
        "merkki" : "Toyota",
        "Malli" : "Corolla",
        "vm" : 1994
    },
    
    {
        "merkki" : "Volvo",
        "malli" : "XC90", 
        "vm" : 2015 
    },
    
    {
        "merkki" : "Kia",
        "malli" : "Ceed",
        "vm" : 2024
    }
]

print(autot[2])

# päätietorakenne (koko lista) + indeksi(mones listalla, muista eka on 0) + avain (merkki))
print(autot[1]["merkki"])   