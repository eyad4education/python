def saisie():
    global n
    valid = False
    while valid == False:
        n = int(input("Entrer n: "))
        valid = 5 <= n <= 30


def remplir(n):
    global t1
    for i in range(n):
        valid = False
        while valid == False:
            t1[i] = str(input("Entrer votre condition: "))
            ch = t1[i]
            valid = len(ch) >= 4 and ch[len(ch)-1] == "="


def generer(t1, n):
    global t2
    for i in range(n):
        t2[i] = somme(t1[i])


def somme(ch):
    x = ch.find("+")
    ch1 = ch[0:x]
    ch2 = ch[x+1:len(ch)-1]
    s = int(ch1)+int(ch2)
    return s


def affiche(t1, t2, n):
    for i in range(n):
        if t2[i] % 2 == 0:
            print(t1[i], t2[i])


saisie()
t1 = [str()]*n
t2 = [int()]*n
remplir(n)
generer(t1, n)
affiche(t1, t2, n)
