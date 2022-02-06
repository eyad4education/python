# ecrire un programme qui permet de trier un matrice M de i colones et j lignes, et afficher CROISOMENT (c) oubien DECORISEMENT (dc)
m = [[7, 3, 1, 4], [2, 5, 9, 11], [8, 0, 6, 10]]
c = 4
l = 3
mt = [int()] * (c*l)
choix = str(input("Croisoment (c) oubien Decroisement (dc): "))
x = 0
for j in range(l):
    for i in range(c):
        if x < l*c:
            mt[x] = m[j][i]
            x += 1
v = False
while v == False:
    p = False
    for i in range(l*c-1):
        if mt[i] > mt[i+1]:
            swp = mt[i]
            mt[i] = mt[i+1]
            mt[i+1] = swp
            p = True
    v = p == False
if choix == "c":
    x = 0
    for j in range(l):
        for i in range(c):
            if x < l*c:
                m[j][i] = mt[x]
                x+=1
    for x in m:
        print(x)
elif choix == "dc":
    nmt = [0] * (l*c)
    for i in range(l*c):
        nmt[i] = mt[(l*c-1)-i]
    x = 0
    for j in range(l):
        for i in range(c):
            if x < l*c:
                m[j][i] = nmt[x]
                x+=1
    for x in m:
        print(x)