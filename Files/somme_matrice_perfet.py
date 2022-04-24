import random
def saisie():
    global n
    v = False
    while not v:
        n = int(input("Donner n: "))
        v = 2 <= n <= 20
def remplir(n):
    for j in range(n):
        for i in range(n):
            # m[j][i] = int(input(f"donner un entier [{j}|{i}]: "))
            m[j][i] = random.randint(1, 999)

def sommeL(m, a, n):
    ch = ""
    for i in range(n):
        ch += str(m[i][a])
    sum = 0
    x = int(ch)
    for i in range(len(ch)):
        sum += x % 10
        x = x // 10
    return sum
def sommeC(m, a, n):
    ch = ""
    for i in range(n):
        ch += str(m[a][i])
    sum = 0
    x = int(ch)
    for i in range(len(ch)):
        sum += x % 10
        x = x // 10
    return sum

def completer_fch(np, n):
    global m
    F = open(np, "w")
    for j in range(n):
        for i in range(n):
            if sommeL(m, j, n) == sommeC(m, i, n):
                F.write("Element " + str(m[j][i]) + " ligne " + str(j+1) + " colonne " + str(i+1) + "\n")
    F.close()

saisie()
m = [([int() for i in range(n)]) for i in range(n)]
remplir(n)
np = "test.txt"
completer_fch(np, n)