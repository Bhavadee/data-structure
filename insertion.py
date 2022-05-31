def sort(l):
    for i in range(len(l)):
        j = i -1
        while j >= 0 and l[j] > l [j+1]:
            tem = l[j]
            l[j] = l[j+1]
            l[j+1] = tem
            
            j = j -1
l = [2,3,1,4,5,6,4]
print(l)
sort(l)
print(l)
