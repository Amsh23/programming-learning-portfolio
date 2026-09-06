a = int(input("enter a number: "))
i = 1
c=0
while i <= a :
    
    if a%i==0:
        print(i)
        c=c+1
        
    i = i + 1

if c==2:
    print("yes")
else:
    print("no")
