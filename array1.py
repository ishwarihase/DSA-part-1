arr=[4,2,8,1,9]
min=arr[0]# take first num in array as smallest
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]

print(min)