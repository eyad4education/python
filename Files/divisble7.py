import pickle as pickle


def saisie():
    global n
    v = True
    while v:
        n = int(input("donner n: "))
        v = not(2 <= n <= 10)


def completer(nf, n):
    F = open(nf, "wb")
    for i in range(n):
        pickle.dump(str(input(f"donner expression numero {i+1} : ")), F)
    F.close()


def calcul(nf, ng):
    F = open(nf, "rb")
    G = open(ng, "wb")
    Fin_Fichier = False
    while not Fin_Fichier:
        try:
            e = {}
            e["s"] = somme(pickle.load(F))
            e["msg"] = divisible(e["s"])
            pickle.dump(e, G)
        except:
            Fin_Fichier = True

    F.close()
    G.close()


def somme(ch):
    sum = 0
    v = False
    while not v and ch.find("+") != -1:
        sum += int(ch[0:ch.find("+")])
        ch = ch[:0] + ch[ch.find("+")+1:]
        # ch = ch[ch.find("+")+1:len(ch)]
        v = ch.find("+") == -1
    sum += int(ch)
    return sum


def divisible(k):
    v = False
    while not v:
        x = k // 10
        y = k % 10
        k = abs(x - 2 * y)
        v = k >= 0 and k <= 9
    if k in [0, 7]:
        ch = "divisible par 7"
    else:
        ch = "NE PAS divisible par 7"
    return ch


def affiche(ng):
    G = open(ng, "rb")
    Fin_Fichier = False
    while not Fin_Fichier:
        try:
            e = pickle.load(G)
            print(e["s"], "    ", e["msg"])
        except:
            Fin_Fichier = True
    G.close()


saisie()
nf = "expression.dat"
completer(nf, n)
ng = "resulat.dat"
calcul(nf, ng)
affiche(ng)
