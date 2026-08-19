my_arr=[7,12,9,11,6]

n=len(my_arr)
'''for i → how many times sorting runs
for j → compare numbers in the list'''
for i in range(n-1):
    for j in range(n-i-1):
        if my_arr[j]>=my_arr[j+1]:
            temp=my_arr[j]
            my_arr[j]=my_arr[j+1]
            my_arr[j+1]=temp
            
print(my_arr)
# timecom=o(2N) ==o(N)
#spacec=o(1)