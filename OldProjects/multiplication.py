valid = False
while valid == False:
    n = int(input("Entrer un nombre entre 1 et 10: "))
    valid = 1 <= n <= 10
m = 0
for i in range(1, 10):
    m = i*n
    print(i, "x", n, "=", m)
