from random import randint


def saisie():
    global n
    v = False
    while v == False:
        n = int(input("Donner n:"))
        v = n > 2


def remplir(n):
    global tnombre
    for i in range(n):
        tnombre[i] = randint(1, 100)


def div(x):
    global nbx, na
    nbx = 1
    s = 0
    for i in range(1, (x//2)+1):
        if x % i == 0:
            nbx += 1
            s += i
    if x == s:
        na = "parfait"
    elif x > s:
        na = "deficient"
    else:
        na = "abondant"


def generer(tnombre, n):
    global tnature
    for i in range(n):
        e = {}
        e["A"] = tnombre[i]
        div(tnombre[i])
        e["nbdv"] = nbx
        e["nat"] = na
        tnature[i] = e


def affiche(tnature, n):
    for i in range(n):
        e = tnature[i]
        print(e["A"], " ", e["nbdv"], " ", e["nat"])


saisie()
tnombre = [int()] * n
remplir(n)
tnature = [{}] * n
generer(tnombre, n)
affiche(tnature, n)
