## Kirjoita ohjelma joka laskee kuinka monessa listan sanassa on yli 5 kirjainta
## Luo itse lista ja käytä len-funktiota tarkistukseen

lista = ["banaani", "omena", "kahvi", "kortti", "auto", "juusto"]

laskuri = 0

for sana in lista:
    if len(sana) > 5:
        laskuri += 1
    
print(f"\nListalla oli yhteensä {laskuri} sanaa, joissa oli yli 5 kirjainta.")