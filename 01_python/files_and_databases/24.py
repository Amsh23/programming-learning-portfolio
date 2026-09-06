while True:
    num1= int(input("enter a number1: "))
    sign= input("enter a sign + - * /: ")
    num2= int(input("enter a number2: "))
    if sign=="+":
        print(num1+num2)
    elif sign=="-":
        print(num1-num2)

    elif sign=="*":
        print(num1*num2)
    elif sign=="/":
        print(num1/num2)
    else:
        print("wrong")
