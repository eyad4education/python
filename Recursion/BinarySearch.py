list = [1,2,3,4,5,6,7,8,9]
start = 0
end = len(list)-1
def binarySearch(list, element, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if list[mid] == element:
        return mid
    if element > list[mid]:
        return binarySearch(list, element, mid+1, end)
    if element < list[mid]:
        return binarySearch(list, element, start, mid-1)
print(binarySearch(list, 8, start, end))