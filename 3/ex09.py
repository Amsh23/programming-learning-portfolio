a=int(input("enter a number1="))
b=int(input("enter a number2="))
c=int(input("enter a number3="))
if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print('yes')
else:
    print('no')
