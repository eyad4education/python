def decompresser(chaine):
    space = " "
    sumspace = 0
    stop = False
    if chaine.find(space) == -1 and chaine.find(space) != len(chaine)-1:
        stop = True
    i = 0
    while not stop and i < len(chaine):
        if chaine[i] == space:
            sumspace += 1
        i += 1
    sumspace+=1
    t = [str()] * sumspace
    old = 0
    for i in range(sumspace):
        if chaine.find(space) != -1:
            index = chaine.find(space)
        else:
            index = len(chaine)
        t[i] = chaine[0:index]
        old = chaine.find(space) + 1
        chaine = chaine[old:len(chaine)]
    och = ""
    for i in range(sumspace):
        ch = t[i]
        fois = int(ch[1:len(ch)])
        for j in range(fois):
            och += ch[0]
    return och


ch1 = "a12 b5 C3 d11"
ch2 = "c13"
ch3 = "A12 b5"
def choix(i):
    switcher={
            1:decompresser(ch1),
            2:decompresser(ch2),
            3:decompresser(ch3)
        }
    return switcher.get(i,"Choix non valide.")
x = 1
while True and x in [1,2,3]:
    print(ch1)
    print(ch2)
    print(ch3)
    x = int(input("Donner votre choix: "))
    print(choix(x),"\n")

