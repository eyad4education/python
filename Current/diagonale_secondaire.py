from random import randint


l = 4
m = [[str()] * l for i in range(l)]
for j in range(l):
    for i in range(l):
        m[j][i] = chr(randint(65, 90))

for i in m:
    print(i)
print()
ch = ""
for i in range(l):
    ch += m[i][l-i-1]

print(ch)
