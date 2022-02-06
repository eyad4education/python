# 18 est un nombre Harshard. puisqu'il est divisble par la somme de ce chiffres.
a = int(input("a="))
b = int(input("b="))
for i in range(a, b):
    x = str(i)
    s = 0
    for j in range(len(x)):
        s += int(x[j])
    if i % s == 0:
        print(i, "est Harshad")
