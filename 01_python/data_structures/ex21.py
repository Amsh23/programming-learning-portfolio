a=int(input("enter a number"))
f=1
for i in range(1,a):
    f=f*i
    print(i,end="*")
print(a,end="=")
print(f*a)
    




a=int(input("enter a number"))
f=1
for i in range(a,1,-1):
    f=f*i
    print(i,end="*")
    
print(1,end="=")
print(f*a)
