def saisie():
    global n
    valid = False
    while valid == False:
        n = int(input("Entrer n: "))
        valid = 2 <= n <= 20


def remplir(n):
    global t
    for i in range(n):
        t[i] = int(input("Entrer un nombre: "))


def min_max(t, n):
    global min, max
    min = t[0]
    max = t[0]
    for i in range(1, n):
        if t[i] < min:
            min = t[i]
        if t[i] > max:
            max = t[i]


saisie()
t = [int()]*n
remplir(n)
min_max(t, n)
print(min, "   ", max)
exit = input("Cliquez sur ENTRER pour sortir...")
