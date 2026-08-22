arr=[10,1,1,1,2,3,4,5,5,4,6,7,8,9,9]
n=len(arr)
i=0
while i<n :
    j=i+1
    while j<n:
        if arr[i]==arr[j]:
            k= j
            while k<n-1:
                arr[k]=arr[k+1]
                k+=1

            n-=1
        else:
            j+=1
    i+=1
print(arr[:n])