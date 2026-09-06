def func (a,b,c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a*b
    elif c =="/":
        return a /b
    else:
        return "wrong"
while True:
    x = int(input("enter number : "))
    y = int(input("enter number : "))
    z = input("enter + , - , * , /")
    print(func(x,y,z))
