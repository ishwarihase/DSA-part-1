'''if 123 = 1^3 +2^3 + 3^3
            =123
or    45667= 4^5 + 5^5 + 6^5 + 6^5 + 7^5
            = 45667 then these num asre armstrong'''

num=int(input())
n=num
len=len(str(num))
total=0
while num>0:
    ld=num%10 # % gives the last digit of the number.
    total=total+(ld ** len)
    num=num//10 #//removes the last digit
if total==n:
    print("yes")
else:
    print("no")
