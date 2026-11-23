c1=0
str1=input("enter str1").lower()
for i in str1:
    if not(i.isalpha() or i.isspace()) :
        c1+=1
if c1>0:
    print("error")
else:
    print("correct")
str2="oeuai"
c=0
for i in str1:
    if i in str2:
        c+=1
print(c)
print(str1.count(" the "))
