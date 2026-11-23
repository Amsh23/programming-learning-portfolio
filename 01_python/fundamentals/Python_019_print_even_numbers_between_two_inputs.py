a=int(input("enter number 1 = "))
b=int(input("enter number 2 = "))
if a>b:
    a,b=b,a
i=a+1
while a<i<b:
    if i%2==00:
        print(i)
    i=i+1
