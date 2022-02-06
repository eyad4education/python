valid = False
while valid == False:
    n = int(input("Donner la nombre de copie/s: "))
    if n <= 10:
        f = n*300
    else:
        if n <= 30 and n > 10:
            f = 10*300 + (n-10)*200
        if n > 30:
            f = 10*300 + 20*200 + (n-30)*100
    print("Le montant que tu vais payer est:", format(f/1000, ".3f"), "TND")
