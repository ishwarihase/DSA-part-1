''''navin ,nitin,aba are pallindrome'''
''' here if n= 1234 then 1) 4*10=40 and 40+3=43
    2) 43*10=430 and 430+2=432 and at last 432*10=4320 and 4320+1=4321 now if this num equals input means it is palindrome'''
n=int(input())
num=n
result=0
while num>0:
    id=num%10 # % gives last element
    result=(result*10) +id
    num=num//10 # // removes last element
if result==n:
    print( n, "is palindrome")
else:
    print(n,"is not palindrome")


