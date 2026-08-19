# brute force solution  TC=O(N)
def func(num):
    result=[]
    
    for i in range(1, num):
        if num % i == 0:
            result.append(i)
            
    return result
print(func(10))


