import string


def saisie():
    global n
    while True:
        n = int(input("Donner n: "))
        if 2 <= n <= 50:
            break


def remplir(n):
    global t
    for i in range(n):
        while True:
            print("Donner l'element numero: ", i+1, ": ", end="")
            t[i] = input()
            if len(t[i]) <= 10:
                break


def calcul(t, n):
    global v
    for i in range(n):
        v[i] = nbre(t[i])


def nbre(ch):
    nb = 0
    chaine = string.ascii_letters
    for i in range(len(ch)):
        if not ch[i] in chaine:
            nb += 1
    return nb


def somme(t, n):
    x = 0
    for i in range(n):
        x += t[i]
    return x


saisie()
t = [str()]*n
remplir(n)
v = [str()]*n
calcul(t, n)
s = somme(v, n)
print("La nombre total de caracteres non alphabetiques est: ", s)
