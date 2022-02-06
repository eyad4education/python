def saisir():
    global x, y
    valid = False
    while valid == False:
        x = int(input("Entrer x: "))
        y = int(input("Entrer y: "))
        valid = x <= 9 and y <= 9
def puissance(x,y):
    a = 1
    for i in range(y):
        a = x*a
    return a
    

saisir()
p = puissance(x,y)
print("La puissance est: ",p)