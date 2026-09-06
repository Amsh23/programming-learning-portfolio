#1
def func01(a):
    f=1
    for i in range (a,1,-1):
        f=f*i
    return f
x=int(input("enter a number"))        
print(func01(x))

#2
def func01(a):
    f=1
    while a>1:
        f=f*a
        a-=1
    return f
x=int(input("enter a number"))        
print(func01(x))
