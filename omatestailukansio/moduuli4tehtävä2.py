# Tee ohjelma joka kysyy tuumia ja muuntaa ne senttimetreiksi.
# oikea ratkaisu joka käyty tunnilla läpi:

# 1 tuuma = 2.54 cm

tuuma = float(input("Anna tuumaluku jonka haluat muuntaa (negatiivinen lopettaa): "))

while tuuma >= 0:
    cm = tuuma * 2.54
    print(f"{tuuma} tuumaa on {cm} senttimetriä.")
    tuuma = float(input("Anna tuumaluku jonka haluat muuntaa (negatiivinen lopettaa): "))
    