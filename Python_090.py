
a=int(input("enter a number:"))
if  100<=a<=999:
    s=a//100
    b=a%100
    d=b//10
    y=b%10
    if d==y:
        print("equal")
    else:
        print("no")
else:
    print("wrong")
