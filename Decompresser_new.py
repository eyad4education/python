def Decompresser(ch):
    ch += " "
    chd = ""
    v = False
    while not v:
        x = int(ch[1:ch.find(" ")])
        for i in range(x):
            chd += ch[0]
        ch = ch[:0] + ch[ch.find(" ")+1:]
        v = ch == ""
    return chd


print(Decompresser("a12 b3 C4"))
