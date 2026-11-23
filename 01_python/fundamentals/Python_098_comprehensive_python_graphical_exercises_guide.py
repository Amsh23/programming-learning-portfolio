import turtle
import time

# ####################################################################################
# راهنمای کامل تمرین‌های برنامه‌نویسی پایتون - با نمایش گرافیکی
# Complete Python Programming Guide - With Graphical Display
# ####################################################################################

def setup_turtle():
    """تنظیمات اولیه turtle برای نمایش گرافیکی"""
    t = turtle.Turtle()
    t.speed(0)  # سریع‌ترین سرعت
    t.pensize(2)
    return t

def clear_screen():
    """پاک کردن صفحه"""
    turtle.clear()
    turtle.reset()

"""
بخش اول: تمرین‌های ساده ورودی/خروجی
Part 1: Basic Input/Output Exercises
"""

# 1. چاپ نام و فاصله (p04 - Copy.py)
def name_spacing_example():
    """
    نمایش روش‌های مختلف چاپ نام با فاصله
    Different ways to print name with spacing
    """
    name = input("enter a name=")
    lastname = input("enter a lastname=")
    print(f"\nروش‌های مختلف چاپ:\n")
    print(name, "        ", lastname)
    print(name, " "*8, lastname)
    print(name+" "*10+lastname)

# 2. محاسبات پایه (p13 - Copy.py)
def basic_calculations():
    """
    انجام محاسبات پایه ریاضی
    Basic mathematical calculations
    """
    a = float(input("enter a number1="))
    b = float(input("enter a number2="))
    summ = a + b
    sub = a - b
    mul = a * b
    div = a/b if b != 0 else "undefined"
    print(f"\nنتایج محاسبات:\n")
    print(f"sum={summ}\nsubtract={sub}\nmultiply={mul}")
    print(f"divide={div if isinstance(div, str) else div:.2f}")

"""
بخش دوم: الگوهای گرافیکی
Part 2: Graphical Patterns
"""

# 3. الگوی مثلث ساده (ex13 - Copy - Copy.py)
def simple_triangle_pattern():
    """
    چاپ و نمایش گرافیکی مثلث ساده
    Print and draw simple triangle pattern
    """
    print("\nالگوی مثلث در متن:")
    for i in range(1, 5):
        print("*" * i)
    
    # نمایش گرافیکی
    t = setup_turtle()
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    
    for i in range(1, 5):
        t.forward(i * 20)  # هر ستاره 20 پیکسل
        t.penup()
        t.goto(-100, 100 - i * 20)
        t.pendown()

# 4. الگوی لوزی (07 - Copy (2).py)
def diamond_pattern():
    """
    چاپ و نمایش گرافیکی الگوی لوزی
    Print and draw diamond pattern
    """
    n = int(input("enter a number (3-7 recommended): "))
    print("\nالگوی لوزی در متن:")
    
    # چاپ متنی
    for i in range(-n+1, n):
        if i < 0:
            i = -i
        space = " " * i
        star = "*" * (2*(n-i)-1)
        print(space + star)
    
    # نمایش گرافیکی
    t = setup_turtle()
    t.penup()
    t.goto(-50*n, 50)
    
    # رسم لوزی
    for i in range(-n+1, n):
        if i < 0:
            i = -i
        spaces = i
        stars = 2*(n-i)-1
        t.penup()
        t.goto(-50*n + spaces*20, 50 - (i+n-1)*20)
        t.pendown()
        t.forward(stars * 20)

"""
بخش سوم: برنامه‌های محاسباتی
Part 3: Calculation Programs
"""

# 5. محاسبه فاکتوریل (ex20 - Copy - Copy.py)
def calculate_factorial():
    """
    محاسبه و نمایش گرافیکی فاکتوریل
    Calculate and visualize factorial
    """
    a = int(input("enter a number (1-7 recommended): "))
    f = 1
    print("\nمراحل محاسبه فاکتوریل:")
    
    for i in range(1, a+1):
        f = f * i
        print(f"{i}! = {f}")
    
    # نمایش گرافیکی
    t = setup_turtle()
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    
    # رسم نمودار رشد فاکتوریل
    prev_y = 0
    for i in range(1, a+1):
        fact = 1
        for j in range(1, i+1):
            fact *= j
        t.goto(-150 + i*30, fact/5)  # مقیاس 1/5 برای نمایش بهتر
        t.dot(5)
        if i > 1:
            t.write(f"{i}! = {fact}")

# 6. تشخیص اعداد اول (ex03 - Copy (3).py)
def find_prime_numbers():
    """
    یافتن و نمایش گرافیکی اعداد اول
    Find and visualize prime numbers
    """
    print("\nاعداد اول تا 20:")
    primes = []
    
    for i in range(1, 21):
        n = 1
        c = 0
        while n <= i:
            if i % n == 0:
                c = c + 1
            n = n + 1
        if c == 2:
            primes.append(i)
            print(i, end=" ")
    
    # نمایش گرافیکی
    t = setup_turtle()
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    
    # رسم نقاط برای اعداد اول
    for prime in primes:
        t.penup()
        t.goto(-200 + prime*20, 0)
        t.pendown()
        t.dot(10, "red")
        t.write(str(prime))

"""
بخش چهارم: برنامه‌های کاربردی
Part 4: Practical Programs
"""

# 7. ماشین حساب ساده (ex19 - Copy.py)
def simple_calculator():
    """
    ماشین حساب ساده با عملیات اصلی
    Simple calculator with basic operations
    """
    print("\nماشین حساب ساده")
    a = float(input("enter your num1: "))
    c = input("what you want to do with numbers(+ - * /): ")
    b = float(input("enter your num2: "))
    
    result = None
    if c == "+":
        result = a + b
    elif c == "-":
        result = a - b
    elif c == "*":
        result = a * b
    elif c == "/" and b != 0:
        result = a / b
    
    if result is not None:
        print(f"Result: {result}")
        
        # نمایش گرافیکی
        t = setup_turtle()
        t.penup()
        t.goto(-100, 0)
        t.write(f"{a} {c} {b} = {result}", font=("Arial", 16, "normal"))

# 8. تبدیل واحد (x1 - Copy.py)
def unit_converter():
    """
    تبدیل ثانیه به دقیقه
    Convert seconds to minutes
    """
    seconds = int(input("enter your seconds: "))
    minn = seconds/60
    print(f"{seconds} seconds = {minn} minutes")
    
    # نمایش گرافیکی
    t = setup_turtle()
    t.penup()
    t.goto(-150, 0)
    
    # رسم خط زمان
    t.pendown()
    t.forward(300)
    t.write("Time Line")
    t.penup()
    t.goto(-150, 20)
    t.write(f"{seconds}s = {minn}m")

def main_menu():
    """منوی اصلی برنامه"""
    while True:
        print("\n=== منوی اصلی برنامه ===")
        print("1. نمایش نام با فاصله")
        print("2. محاسبات پایه")
        print("3. الگوی مثلث")
        print("4. الگوی لوزی")
        print("5. محاسبه فاکتوریل")
        print("6. نمایش اعداد اول")
        print("7. ماشین حساب ساده")
        print("8. تبدیل واحد")
        print("0. خروج")
        
        choice = input("\nلطفاً شماره تمرین مورد نظر را وارد کنید (0-8): ")
        
        if choice == "0":
            print("برنامه به پایان رسید. موفق باشید!")
            break
            
        functions = {
            "1": name_spacing_example,
            "2": basic_calculations,
            "3": simple_triangle_pattern,
            "4": diamond_pattern,
            "5": calculate_factorial,
            "6": find_prime_numbers,
            "7": simple_calculator,
            "8": unit_converter
        }
        
        if choice in functions:
            clear_screen()  # پاک کردن صفحه قبل از هر نمایش جدید
            functions[choice]()
            input("\nPress Enter to continue...")
            clear_screen()
        else:
            print("لطفاً عدد صحیح بین 0 تا 8 وارد کنید.")

if __name__ == "__main__":
    print("به راهنمای جامع برنامه‌نویسی پایتون خوش آمدید!")
    print("این برنامه شامل نمایش گرافیکی الگوها و محاسبات است.")
    main_menu()
    turtle.bye()  # بستن پنجره turtle در پایان برنامه
