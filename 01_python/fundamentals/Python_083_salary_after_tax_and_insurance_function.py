def func01(a,b,c):
    return a - a*b - a*c
x = float(input("enter a salary: "))
y = float(input("enter a tax: "))
z = float(input("enter a insurance: "))
print(func01(x,y,z))
