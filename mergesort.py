def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        merge(L,M,array)

        
def merge(L,M,array):
        i = 0
        j = 0
        k = 0
        m = len(L)
        u = len(M)
        while i <  m and j < u:
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
                k += 1
               
            else:
                array[k] = M[j]
                j += 1
                k += 1
             
        while i < m:
            array[k] = L[i]
            i += 1
            k += 1
         

        while j < u:
            array[k] = M[j]
            j += 1
            k += 1

array = [6, 5, 12, 10, 9, 1]
print("array is :",array)
mergeSort(array)
print("Sorted array is: ",array)

