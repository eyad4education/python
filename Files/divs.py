import pickle as pickle
def saisie():
    global n
    v = False
    while not v:
        n = int(input("Donner un entier: "))
        v = n > 1

def divs(nomphy, n):
    F = open(nomphy, "wb")
    for i in range(1,(n//2)+1): # Pour le nombre premier (1, (n//2)+1, 2)
        if n % i == 0:
            pickle.dump(i, F)
    pickle.dump(n, F)
    F.close()

def output(nomphy):
    F = open(nomphy, "rb")
    Fin_Fichier = False
    while not Fin_Fichier:
        try:
            print(pickle.load(F))
        except:
            Fin_Fichier = True
    F.close()



# saisie()
n = 20
nomphy = "divs.dat"
divs(nomphy, n)
output(nomphy)