def qucik_sort(a,l,n):
  if(l<n):
    p = a[l]
    i = l+1
    j = n
    while(i < j):
        while(i < n and p > a[i]):
            i+=1
        while(j > l and p < a[j]):
            j-=1
        if (i < j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            
    temp = a[j]
    a[j] = a[l]
    a[l] = temp
    qucik_sort(a,l,j-1)
    qucik_sort(a,j+1,n)
  else:
      return

a = [1,3,4,2,5,6]
print(a)
qucik_sort(a,0,len(a)-1)
print(a)

