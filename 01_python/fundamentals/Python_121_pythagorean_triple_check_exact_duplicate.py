a=float(input("enter a numbera"))
b=float(input("enter a numberb"))
c=float(input("enter a numberc"))
if b**2==a**2+c**2:
    print("yes")
elif a**2==b**2+c**2:
    print("yes")
elif c**2==a**2+b**2:
    print("yes")
else:
    print("no")
