# append=lisää, remove=poista, extend=lisää toinen lista, index=
# sort= lajittelee aakkosjärjestykseen
# print(nimet.index("Matti")) tai print("Matin indeksi on", nimet.index("Matti"))


nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

nimet2 = ["Matti", "Teppo"]

nimet.extend(nimet2)

print(nimet)
nimet.sort()

print(nimet)
