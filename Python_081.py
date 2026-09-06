a= float(input("enter your num1 : "))
c = input("what you want to do with numbers(+ - * /) : ")
b = float(input("enter your num2 : "))

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else:
    print("wrong")
