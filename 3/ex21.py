#1 nested if
a=int(input("enter a number:"))
if  10<=a<=99:
    d=a//10
    y=a%10
    if d==y:
        print("equal")
    else:
        print("no")
else:
    print("wrong")



#2
a=int(input("enter a number:"))
if  10<=a<=99 and a%11==0:
    print("yes")
else:
    print("no")
