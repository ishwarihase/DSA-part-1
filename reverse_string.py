s=input()
word=""
result=""
for ch in s:
    if ch != " ":
        word+=ch
    else:
        result = word + " " + result
        word=""
result = word + " " + result
print(result)