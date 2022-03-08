ap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
v1=False
while v1==False:
    ch = input()
    i=-1
    v2 = False
    while v2==False:
        i = i + 1
        v2= not(ch[i] in ap) or i == len(ch)-1
    v1= ch[i] in ap and len(ch) <= 25
print("Accepte")