num1=float(input("enter number"))
num2=float(input("enter number"))
num3=float(input("enter number"))
if num1**2==num2**2+num3**2 or num2**2==num1**2+num3**2  or num3**2==num2**2+num1**2:
  print("yes")
else:
  print("no")