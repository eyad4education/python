n = int(input("Entrer n: "))
s = 0
# Method 1
# j = 1
# for i in range(n):
#     s = s + (j**2)
#     j = j + 2

# Method 2
for i in range(1, n*2+1, 2):
    s = s + i**2
    print(i)
print(s)
