def saisir():
    global n
    v = False
    while v == False:
        n = int(input("Donner n:"))
        v = 2 <= n <= 120


def remplir(n):
    global t
    for i in range(n):
        e = {}
        v = False
        while v == False:
            e["nom"] = str(input("Donner nom:"))
            v = len(e["nom"]) <= 30
        e["ident"] = int(input("Donner ident:"))
        v = False
        while v == False:
            e["tel"] = str(input("Donner tel:"))
            v = len(e["tel"]) <= 10
        e["ncb"] = int(input("Donner ncb: "))
        v = False
        while v == False:
            e["gd"] = str(input("Donner grade:"))
            v = e["gd"] in ["A", "B", "C"]
        t[i] = e


def affiche(t, n):
    for i in range(n):
        e = t[i]
        print(e["nom"], " ", e["ident"], " ",
              e["ncb"], " ", e["tel"], " ", e["gd"])


def nombre(t, n):
    nb = 0
    for i in range(n):
        e = t[i]
        if e["gd"] == "A":
            nb += 1
    return nb


saisir()
t = [{}] * n
remplir(n)
affiche(t, n)
nb = nombre(t, n)
p = (nb/n) * 100
print("le nombre de employee qui ont la grade A est",nb, "et le percentage est", p)