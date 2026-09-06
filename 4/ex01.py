maxnum = float(input("enter a number: "))
num2 = float(input("enter a number: "))
num3 = float(input("enter a number: "))
num4 = float(input("enter a number: "))
num5 = float(input("enter a number: "))

if num2 > maxnum:
    maxnum = num2
if num3 > maxnum:
    maxnum = num3
if num4 > maxnum:
    maxnum = num4
if num5 > maxnum:
    maxnum = num5

print(f"The largest number: {maxnum}")
