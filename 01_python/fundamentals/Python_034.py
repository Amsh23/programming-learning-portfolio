num = int(input("enter a number between 1000 to 9999 : "))
if 1000<=a<=9999: 
    a = num // 1000
    b = num % 10
    if a == b :
        print("true")
    else:
        print("false")
else:
    print("error")
