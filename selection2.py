nums=list(map(int,input().split()))
n=len(nums)

for i in range(0,n):
    min_index=i
    for j in range(i+1,n):
        if nums[min_index] > nums[j]:
            min_index=j
    nums[min_index] ,nums[i] = nums[i],nums[min_index] 
print(nums)