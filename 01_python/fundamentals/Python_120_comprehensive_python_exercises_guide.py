########################################################################################
# راهنمای جامع تمرین‌های برنامه‌نویسی پایتون
# Python Programming Exercises Complete Guide
########################################################################################

# Exercise 1: Finding the Maximum Number
# تمرین ۱: پیدا کردن بزرگترین عدد
###########################################################
def find_maximum():
    """
    این تابع ۵ عدد از ورودی دریافت می‌کند و بزرگترین آنها را چاپ می‌کند
    This function takes 5 numbers as input and prints the largest one
    
    نکات آموزشی:
    - استفاده از متغیرهای float برای اعداد اعشاری
    - استفاده از دستورات شرطی if
    - مقایسه اعداد با یکدیگر
    """
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

# Exercise 2: Pattern Printing - Simple Triangle
# تمرین ۲: چاپ الگو - مثلث ساده
###########################################################
def print_simple_triangle():
    """
    این تابع یک مثلث ساده با ستاره چاپ می‌کند
    This function prints a simple triangle pattern using asterisks
    
    نکات آموزشی:
    - استفاده از حلقه for
    - ضرب رشته‌ها در عدد برای تکرار
    - کار با فضای خالی و کاراکترها
    """
    for i in range(5):
        print("*" * i)

# Exercise 3: Pattern Printing - Rectangle
# تمرین ۳: چاپ الگو - مستطیل
###########################################################
def print_rectangle():
    """
    این تابع یک مستطیل با ستاره چاپ می‌کند
    This function prints a rectangle pattern using asterisks
    
    نکات آموزشی:
    - حلقه‌های تو در تو
    - ثابت نگه داشتن تعداد ستاره‌ها در هر خط
    """
    for i in range(3):
        print("*" * 4)

# Exercise 4: Pattern Printing - Shifted Rectangle
# تمرین ۴: چاپ الگو - مستطیل با جابجایی
###########################################################
def print_shifted_rectangle():
    """
    این تابع یک مستطیل را با فاصله از لبه چاپ می‌کند
    This function prints a rectangle pattern with increasing indentation
    
    نکات آموزشی:
    - ترکیب فضای خالی و کاراکتر
    - استفاده از عملگر + برای ترکیب رشته‌ها
    """
    for i in range(4):
        print(" " * i + "*" * 4)

# Exercise 5: Factorial Calculator
# تمرین ۵: محاسبه فاکتوریل
###########################################################
def calculate_factorial():
    """
    این تابع فاکتوریل عدد ورودی را محاسبه می‌کند
    This function calculates the factorial of an input number
    
    نکات آموزشی:
    - محاسبات ریاضی در حلقه
    - کار با متغیر تجمعی
    - استفاده از range با مقادیر شروع و پایان
    """
    a = int(input("enter a num: "))
    f = 1
    for i in range(1, a + 1):
        f = f * i
    print(f)

# Exercise 6: Diamond Pattern
# تمرین ۶: چاپ الگوی لوزی
###########################################################
def print_diamond():
    """
    این تابع یک الگوی لوزی شکل با ستاره چاپ می‌کند
    This function prints a diamond pattern using asterisks
    
    نکات آموزشی:
    - محاسبه فضای خالی و ستاره‌ها با فرمول
    - استفاده از عملیات ریاضی در الگوها
    """
    a = int(input("enter a number: "))
    for i in range(a):
        print(" " * (a-i-1) + "*" * (2*i+1))
    # می‌توانید بخش پایین لوزی را هم اضافه کنید
    # You can add the bottom half of the diamond here

# نحوه استفاده از توابع
# How to use these functions
if __name__ == "__main__":
    print("Choose an exercise to run:")
    print("1: Find Maximum Number")
    print("2: Simple Triangle Pattern")
    print("3: Rectangle Pattern")
    print("4: Shifted Rectangle Pattern")
    print("5: Factorial Calculator")
    print("6: Diamond Pattern")
    
    choice = input("Enter exercise number (1-6): ")
    
    if choice == "1":
        find_maximum()
    elif choice == "2":
        print_simple_triangle()
    elif choice == "3":
        print_rectangle()
    elif choice == "4":
        print_shifted_rectangle()
    elif choice == "5":
        calculate_factorial()
    elif choice == "6":
        print_diamond()
    else:
        print("Invalid choice!")

########################################################################################
# نکات مهم برای امتحان:
# Important Notes for Exam:
########################################################################################
"""
۱. ساختارهای کنترلی (Control Structures):
   - if, elif, else برای تصمیم‌گیری
   - حلقه‌های for برای تکرار
   - کار با range() برای ایجاد دنباله‌های عددی

۲. متغیرها و انواع داده (Variables and Data Types):
   - اعداد صحیح (int)
   - اعداد اعشاری (float)
   - رشته‌ها (str)
   - تبدیل انواع داده با ()int و ()float

۳. ورودی و خروجی (Input/Output):
   - دریافت ورودی با ()input
   - چاپ با ()print
   - فرمت‌بندی رشته‌ها با f-string

۴. عملگرها (Operators):
   - عملگرهای ریاضی (+, -, *, /, %)
   - عملگرهای مقایسه‌ای (<, >, ==, !=)
   - عملگرهای منطقی (and, or, not)

۵. کار با الگوها (Pattern Work):
   - ضرب رشته‌ها در عدد برای تکرار
   - ترکیب فضای خالی و کاراکترها
   - محاسبه فضای خالی و کاراکترها با فرمول

۶. توابع ریاضی (Mathematical Functions):
   - محاسبه فاکتوریل
   - کار با متغیرهای تجمعی
   - محاسبات ساده ریاضی
"""
