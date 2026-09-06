smallest= float(input("1 - Enter a number: "))
i = 1
while i <= 9:
    num = float(input(f"{i+1} - Enter a number: "))
    if num < smallest:
        smallest = num
    i += 1
print("Smallest number is:", smallest)
