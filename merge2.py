def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
 
        inv_count = mergeSort(L)
        inv_count += mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                inv_count += (len(L)-i)
 
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
        return inv_count
 
    else:
        return 0

array = [3, 1, 5, 2, 4]
array = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

print(mergeSort(array))