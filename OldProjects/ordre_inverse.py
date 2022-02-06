n = 5
TE = [int()]*n
TS = [int()]*n
for i in range(n):
    print("Donner l'element numero",i+1,": ", end="")
    TE[i]= int(input())
for i in range(n):
    TS[(n-1)-i] = TE[i]
print(TS)