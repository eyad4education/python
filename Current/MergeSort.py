def MergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        MergeSort(left)
        MergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i +=1
            else:
                array[k] = right[j]
                j += 1
            k +=1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    

def PrintList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print()

if __name__ == '__main__':
    array = [3,2,4,1]
    MergeSort(array)
    print("The sorted array is: ")
    PrintList(array)