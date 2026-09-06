def func (a,b,c):
    minn = a
    if b < a :
        minn = b
    if c<b:
        minn = c
    return minn

x= int(input("enter your number :"))
z= int(input("enter your number :"))
y= int(input("enter your number :"))
print(func(x,z,y))
