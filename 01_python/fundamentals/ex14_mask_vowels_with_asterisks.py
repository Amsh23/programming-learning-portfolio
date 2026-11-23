str1=input("enter string")
str2="IiOoUuAaEe"
result=''
for i in str1:
    if i in str2:
        result+="*"
    else:
        result+=i
print(result)