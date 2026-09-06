a=int(input("enter number 1 = "))
b=int(input("enter number 2 = "))
if a>b:
    a,b=b,a
if a%2==0:
    a=a+2
else:
    a=a+1
while a<b:
    print(a)
    a=a+2
