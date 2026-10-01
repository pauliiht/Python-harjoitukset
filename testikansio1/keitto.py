## kirjoita ohjelma keittokaupppaa varten

nimi = input("Anna nimesi: ")


if nimi == "Matti":
    print("Seuraava kiitos!")

else:
    annos = int(input("Anna annosten määrä: "))
    print(f"Keittoannoksia on {annos} ja hinta on: {5.90 * annos}")
    print("Seuraava kiitos!")