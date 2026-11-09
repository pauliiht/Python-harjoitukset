##Avaimet ja arvot voi listata haluammallaan tavalla, peräkkäin tai allekkain, ei vaikuta lopputulemaan

puhelinluettelo = {"Viivi" : "050-1234567",
                    "Ahmed" : "040-1112223",
                    "Pekka" : "050-7654321"
                    }

print(puhelinluettelo)

##Pekalla vaihtuu puhelinnumero:
puhelinluettelo["Pekka"] = "045-7654321"

print(puhelinluettelo)

# Uuden arvon lisääminen
puhelinluettelo["Olga"] = "050-1011012"

# Arvon poistaminen
del puhelinluettelo["Viivi"]

print(puhelinluettelo)

## Tulostaa avaimet, eli nimet
for numero in puhelinluettelo:
    print(numero)
  
#Tulostaa arvot, eli puhelinnumerot  
for numero in puhelinluettelo.values():
    print(numero)
    
# Tulostetaan molemmat
for avain, numero in puhelinluettelo.items():
    print(f"{avain}n puhelinnumero on {numero}")