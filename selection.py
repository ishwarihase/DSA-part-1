arr=[3,56,34,76,23,98,23,11,4,5,67]

for i in range(len(arr)-1):
    min_val=i
    for j in range(i+1 , len(arr)):
        if arr[j]<arr[min_val]:
            min_val=j
    min_value=arr.pop(min_val)
    arr.insert(i,min_value)




print("Sorted array:", arr)
            