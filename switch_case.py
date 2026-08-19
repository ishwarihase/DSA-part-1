print("#-----------days by numbers----------")
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")
ch=int(input("enter number:"))
if ch==1:
    print("sunday")
elif ch==1:
    print("monday")
elif ch==2:
    print("tuesday")
elif ch==4:
    print("wednesday")
elif ch==5:
    print("thirsday")
elif ch==6:
    print("friday")
elif ch==7:
    print("saturday")



    days = ["Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"]

ch = int(input("Enter number: "))

if 1 <= ch <= 7:
    print(days[ch-1])
else:
    print("Invalid")