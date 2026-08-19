nums = [4, 6, 2, 5, 7, 9, 1, 3]
n=len(nums)
large=float('-inf')
secondl=float('-inf')
for i in range(0,n):
    if nums[i]>large:
        large=nums[i]
for i in range(0,n) :       
    if nums[i]<large and nums[i]>=secondl:
        secondl=nums[i]
               
   

print(secondl)

