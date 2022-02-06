year = int(input("Entrer l'annee: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year, "est Bessextile.")
else:
    print(year, "n'est pas Bessextile")
