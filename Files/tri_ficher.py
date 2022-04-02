import pickle as pickle

def completer(nomphy, n):
    F = open(nomphy, "wb")
    for i in range(n):
        e = {}
        e["nom"] = str(input(f"nom {i+1}: "))
        e["moy"] = float(input(f"moyenne {i+1}: "))
        pickle.dump(e, F)
    F.close()
def tri_fichier(nomphy, t, n):
    F = open(nomphy, "rb")
    for i in range(n):
        t[i] = pickle.load(F)
    v = False
    while not v:
        trier = True
        for i in range(n-1):
            if t[i]["moy"] < t[i+1]["moy"]:
                swap = t[i]
                t[i] = t[i+1]
                t[i+1] = swap
                trier = False
        v = trier
    F.close()
    F = open(nomphy, "wb")
    for i in range(n):
        e = t[i]
        pickle.dump(e, F)
    F.close()

def show(nomphy, n):
    F = open(nomphy, "rb")
    for i in range(n):
        e = pickle.load(F)
        print(e["nom"], "   ", e["moy"])
    F.close()


nomphy = "tri_ficher.dat"
n = 3
completer(nomphy, n)
t = [{}] * n
tri_fichier(nomphy, t, n)
show(nomphy, n)