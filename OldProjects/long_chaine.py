valid = False
while valid==False:
    n=int(input("Donner n: "))
    valid=2<=n<=20
T=n*[str()]
for i in range(n):
    valid=False
    while valid==False:
        print("Entrer la chaine numero",i+1,": ",end="")
        T[i]=str(input())
        valid=len(T[i])>i
ch=T[0]
for i in range(1,n):
    if len(T[i])>len(ch):
        ch=T[i]
print("La plus grand chaine est:",ch)