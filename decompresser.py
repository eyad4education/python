def decompresser(chaine):
    space = " "
    sumspace = 1
    stop = False
    if chaine.find(space) == -1 and chaine.find(space) != len(chaine)-1:
        stop = True
    i = 0
    while stop == False and i < len(chaine):
        if chaine[i] == space:
            sumspace += 1
        i += 1
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


print(decompresser("a12 b5 C3 d11"))
