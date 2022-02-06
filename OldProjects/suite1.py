n = int(input("Entrer la rang: "))
u = int(input("Donner la premier terme de la suite (U0): "))
for i in range(n):
    u = 4 * u + 10
print("U", n, "=", u)
