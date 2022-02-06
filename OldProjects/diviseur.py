while True:
    n = int(input("Donner n: "))
    if n > 0:
        break
x = ""
print("La diviseur de",n,"sont: ",end="")
for i in range(1,n+1):
    if n % i == 0:
        x = x + str(i) + " "
print(x)