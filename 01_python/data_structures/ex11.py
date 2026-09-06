a=set()
for i in range(10):
    number=int(input("Enter a Number:"))
    a.add(number)
print(a)
x=input("enter number=")
a.discard(x)
print(a)