b=[5,4,3,2,1]
start=0
end=(len(b)-1)
while start<end:
    temp=b[start]
    b[start]=b[end]
    b[end]=temp
    start+=1
    end-=1
    print(b)