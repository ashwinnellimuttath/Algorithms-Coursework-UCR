array = [3, 1, 5, 2, 4]
array = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

n = int(input())
array = list(map(int, input().split()))


def mergeSort(array, start, end):
    # count = 0
    if (end -start + 1 <= 1):
        return 0

    mid = (end+start)//2

    # print(count)
    count = mergeSort(array,start, mid)
    count += mergeSort(array,mid + 1, end)

    # print(count)
    count = merge(array, start,mid,end, count)

    return count

def merge(array, start,mid,end,count):
    L = array[start:mid + 1]
    R = array[mid + 1: end + 1]

    i = 0
    j = 0
    k = start
    

    while i < len(L) and j < len(R):

        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
            count += (len(L)-i)
        k += 1

    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
        # count += 1

    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1   
        # count += 1

    return count


c = mergeSort(array,0,len(array))
print(c)