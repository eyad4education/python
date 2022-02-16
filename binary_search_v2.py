n = 20
number = 18
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
start = 0
end = n-1
found = False
v = False
while v == False:
    mid = (end+start)//2
    if list[mid] == number:
        found = True
        index = mid
    elif number > list[mid]:
        start = mid+1
    elif number < list[mid]:
        end = mid-1
    v = (found) or (start > end)
if found == True:
    print("Found in index ", index)
else:
    print("Not found.")
