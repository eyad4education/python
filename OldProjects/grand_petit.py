n=int(input("Entrer un nombre entre 1 et 10: "))
while n>20 or n<10:
    if n<10:
        print("Plus petit!")
    elif n>20:
        print("Plus grand")
    n=int(input("Entrer un nombre entre 10 et 20: "))
print("Bravo!")
