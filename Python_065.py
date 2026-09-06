def funcw(a):
    if a>0:
        return "positive"
    elif a<0:
        return "negative"
    else:
        return "zero"
x = int(input("enter a number: "))
print(funcw(x))
