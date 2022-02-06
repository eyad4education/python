while True:
    n = int(input("Entrer un nombre: "))
    if n < 0:
        print("Entrer un Nombre postitive!")
    if n >= 0:
        break
if n == 0:
    print("La factorielle de 0 est 1.")
else:
    f = 1
    for i in range(2, n+1):
        f = f * i
    print("La factorielle de", n, "est: ", f)
