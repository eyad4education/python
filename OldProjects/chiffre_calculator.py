def saisir():
    global n
    while True:
        n = int(input("Donner n: "))
        if 2 <= n <= 30:
            break


def remplir(n):
    global t
    for i in range(n):
        valid = False
        while valid == False:
            print("Donner la chaine numero", i+1, ": ", end="")
            t[i] = input()
            valid = len(t[i]) >= 4


def check(t, n):
    global s
    sc = ""
    c = [str()]*n
    chiffr = "0123456789"
    for i in range(n):
        if t[i] in chiffr:
            sc = sc + sc[t[i]]
            c[i] = sc
    s = 0
    for i in range(n):
        s = s + int(c[i])
    print("La somme est: ", s)


saisir()
t = [str()]*n
remplir(n)
check(t, n)
