temp = int(input("Donner la temps en seconds: "))
h = temp//3600
m = temp % 3600//60
s = temp % 60
print(h, "heure/s:", m, "minute/s:", s, "second/s")
