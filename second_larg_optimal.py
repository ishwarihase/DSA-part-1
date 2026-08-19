nums = [4, 6, 2, 5, 7, 9, 1, 3]
n=len(nums)
large=float('-inf')
secondl=float('-inf')
for i in range(n):
    if nums[i]>large:
        secondl=large
        large=nums[i]
    elif nums[i]>secondl and nums[i]!=large:
        secondl=nums[i]

print(secondl)

# timecom=0(N)
# spac com=o(1)