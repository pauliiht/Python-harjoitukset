# append=lisää, remove=poista, extend=lisää toinen lista, index=
# print(nimet.index("Matti")) tai print("Matin indeksi on", nimet.index("Matti"))


nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

nimet2 = ["Matti", "Teppo"]

nimet.extend(nimet2)

print(nimet)
if "Matti" in nimet:
    print("Matin indeksi on", nimet.index("Matti"))
else:
    print("Mattia ei löytynyt listalta.")