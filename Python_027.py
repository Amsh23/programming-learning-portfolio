# ####################################################################################
# راهنمای جامع تمرین‌های برنامه‌نویسی پایتون - شامل تمام مثال‌ها
# Complete Python Programming Guide - Including All Examples
# ####################################################################################

"""
بخش اول: تمرین‌های پایه
Part 1: Basic Exercises
"""

# 1. چاپ نام و نام خانوادگی (0000 - Copy.py)
def print_name():
    """
    این تمرین نحوه چاپ متن و استفاده از پارامتر end را نشان می‌دهد
    """
    print("fatemeh", end=' ')  # end=' ' باعث می‌شود خط جدید ایجاد نشود
    print("rafiepour")

# 2. محاسبه تخفیف قیمت (01 - Copy (2).py)
def calculate_discount():
    """
    این تمرین محاسبه 11% تخفیف روی قیمت‌ها را نشان می‌دهد
    """
    for i in range(15):
        price = float(input(f"cost{i+1}="))
        print(price * 0.89)  # 89% قیمت اصلی (11% تخفیف)

# 3. نمایش اعداد زوج بین دو عدد (01 - Copy (3).py)
def print_even_numbers():
    """
    این تمرین نمایش اعداد زوج بین دو عدد ورودی را نشان می‌دهد
    """
    a = int(input("enter number 1 = "))
    b = int(input("enter number 2 = "))
    if a > b:  # مرتب‌سازی اعداد
        a, b = b, a
    i = a + 1
    while a < i < b:
        if i % 2 == 0:
            print(i)
        i = i + 1

# 4. تشخیص عدد سه رقمی (3digitnum.py)
def check_three_digit():
    """
    این تمرین تشخیص می‌دهد که آیا عدد ورودی سه رقمی است یا خیر
    """
    num = int(input("enter num: "))
    if num > 100:
        print("its 3digit number")
    else:
        print("its not 3digit")

# 5. چاپ الگوی مستطیل (04 - Copy (2).py)
def print_rectangle_pattern():
    """
    این تمرین چاپ یک مستطیل با ستاره را نشان می‌دهد
    """
    for i in range(3):
        print("*" * 6)

# 6. چاپ الگوی لوزی (05 - Copy (2).py)
def print_diamond_pattern():
    """
    این تمرین چاپ یک الگوی لوزی پیچیده‌تر را نشان می‌دهد
    """
    for i in range(5):
        if i < 3:
            print(" " * (2-i), "*" * (2*i+1))
        else:
            print(" " * (i-2), "*" * (9-2*i))

# 7. چاپ لوزی با ورودی کاربر (07 - Copy (2).py)
def print_custom_diamond():
    """
    این تمرین چاپ لوزی با اندازه دلخواه را نشان می‌دهد
    """
    n = int(input("enter a number: "))
    for i in range(-n+1, n):
        if i < 0:
            i = -i
        space = " " * i
        star = "*" * (2*(n-i)-1)
        print(space + star)

# 8. چاپ اعداد فرد دو رقمی (08 - Copy (2).py)
def print_odd_two_digit():
    """
    این تمرین چاپ اعداد فرد دو رقمی را نشان می‌دهد
    """
    i = 11
    while i <= 99:
        print(i, end=" ")
        i = i + 2

# 9. جمع ده عدد (10 - Copy (2).py)
def sum_ten_numbers():
    """
    این تمرین محاسبه مجموع ده عدد ورودی را نشان می‌دهد
    """
    i, s = 1, 0
    while i <= 10:
        a = int(input("enter a number: "))
        s = s + a
        i = i + 1
    print(s)

# 10. تشخیص زوج و فرد (11 - Copy (2).py)
def check_even_odd():
    """
    این تمرین تشخیص زوج یا فرد بودن ده عدد را نشان می‌دهد
    """
    i = 1
    while i <= 10:
        a = int(input(f"enter a number{i}: "))
        if a % 2 == 0:
            print("even")
        else:
            print("odd")
        i = i + 1

# 11. یافتن کوچکترین عدد (13 - Copy (2).py)
def find_smallest():
    """
    این تمرین یافتن کوچکترین عدد از بین ده عدد را نشان می‌دهد
    """
    smallest = float(input("1 - Enter a number: "))
    i = 1
    while i <= 9:
        num = float(input(f"{i+1} - Enter a number: "))
        if num < smallest:
            smallest = num
        i += 1
    print("Smallest number is:", smallest)

# 12. محاسبه میانگین اعداد مثبت (19 - Copy (2).py)
def calculate_positive_average():
    """
    این تمرین محاسبه میانگین اعداد مثبت را نشان می‌دهد
    """
    a = int(input("enter a number: "))
    c = 0
    s = 0
    while a >= 0:
        s = s + a
        c = c + 1
        a = int(input("enter a number: "))
    print(s/c)

"""
بخش دوم: توابع و توابع بازگشتی
Part 2: Functions and Recursive Functions
"""

# 13. تابع جمع دو عدد (ex06 - Copy (3).py)
def add_numbers():
    """
    این تمرین تعریف و استفاده از تابع برای جمع دو عدد را نشان می‌دهد
    """
    def func01(a, b):
        return a + b
    
    x = int(input("enter a number: "))
    y = int(input("enter a number: "))
    print(func01(x, y))

# 14. تابع محاسبه میانگین (ex07 - Copy (3).py)
def calculate_average():
    """
    این تمرین محاسبه میانگین سه عدد با استفاده از تابع را نشان می‌دهد
    """
    def funcavg(a, b, c):
        return (a + b + c) / 3
    
    x = int(input("enter a number: "))
    y = int(input("enter a number: "))
    z = int(input("enter a number: "))
    print(funcavg(x, y, z))

"""
بخش سوم: شرط‌های پیشرفته
Part 3: Advanced Conditions
"""

# 15. بررسی مثلث قائم‌الزاویه (ex09 - Copy.py)
def check_right_triangle():
    """
    این تمرین تشخیص مثلث قائم‌الزاویه را نشان می‌دهد
    """
    a = int(input("enter a number1="))
    b = int(input("enter a number2="))
    c = int(input("enter a number3="))
    if (a**2 + b**2 == c**2 or 
        a**2 + c**2 == b**2 or 
        b**2 + c**2 == a**2):
        print('yes')
    else:
        print('no')

# 16. محاسبه حقوق با مالیات (ex20 - Copy (3).py)
def calculate_salary():
    """
    این تمرین محاسبه حقوق با کسر مالیات و بیمه را نشان می‌دهد
    """
    def func01(a, b, c):
        return a - a*b - a*c
    
    x = float(input("enter a salary: "))
    y = float(input("enter a tax: "))
    z = float(input("enter a insurance: "))
    print(func01(x, y, z))

"""
نکات مهم برای امتحان:
Important Exam Tips:
"""

def exam_tips():
    """
    ۱. ورودی و خروجی:
       - استفاده از input() برای دریافت ورودی
       - تبدیل نوع با int() و float()
       - استفاده از f-string برای خروجی
    
    ۲. حلقه‌ها:
       - while برای تکرار با شرط
       - for برای تکرار با تعداد مشخص
       - استفاده از range() با پارامترهای مختلف
    
    ۳. شرط‌ها:
       - if, elif, else برای تصمیم‌گیری
       - عملگرهای مقایسه‌ای
       - شرط‌های ترکیبی با and و or
    
    ۴. توابع:
       - تعریف تابع با def
       - پارامترها و مقادیر برگشتی
       - توابع با پارامترهای پیش‌فرض
    
    ۵. الگوها:
       - استفاده از * برای تکرار رشته
       - کنترل فضای خالی با متد format
       - ترکیب رشته‌ها
    
    ۶. عملیات ریاضی:
       - عملگرهای اصلی (+, -, *, /, %)
       - توان و جذر
       - تبدیل واحدها
    """
    pass

# منوی اصلی برنامه
def main():
    while True:
        print("\n=== منوی اصلی برنامه ===")
        print("1. چاپ نام و نام خانوادگی")
        print("2. محاسبه تخفیف قیمت")
        print("3. نمایش اعداد زوج")
        print("4. تشخیص عدد سه رقمی")
        print("5. چاپ الگوی مستطیل")
        print("6. چاپ الگوی لوزی")
        print("7. چاپ لوزی با ورودی کاربر")
        print("8. چاپ اعداد فرد دو رقمی")
        print("9. جمع ده عدد")
        print("10. تشخیص زوج و فرد")
        print("11. یافتن کوچکترین عدد")
        print("12. محاسبه میانگین اعداد مثبت")
        print("13. تابع جمع دو عدد")
        print("14. تابع محاسبه میانگین")
        print("15. بررسی مثلث قائم‌الزاویه")
        print("16. محاسبه حقوق با مالیات")
        print("0. خروج")
        
        choice = input("\nلطفاً شماره تمرین مورد نظر را وارد کنید (0-16): ")
        
        functions = {
            "1": print_name,
            "2": calculate_discount,
            "3": print_even_numbers,
            "4": check_three_digit,
            "5": print_rectangle_pattern,
            "6": print_diamond_pattern,
            "7": print_custom_diamond,
            "8": print_odd_two_digit,
            "9": sum_ten_numbers,
            "10": check_even_odd,
            "11": find_smallest,
            "12": calculate_positive_average,
            "13": add_numbers,
            "14": calculate_average,
            "15": check_right_triangle,
            "16": calculate_salary
        }
        
        if choice == "0":
            print("برنامه به پایان رسید. موفق باشید!")
            break
        elif choice in functions:
            functions[choice]()
        else:
            print("لطفاً عدد صحیح بین 0 تا 16 وارد کنید.")
        
        input("\nبرای ادامه کلید Enter را فشار دهید...")

if __name__ == "__main__":
    main()
