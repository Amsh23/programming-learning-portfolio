a=int(input("enter a number"))
f1=1
f2=1
print(f1,f2,end=' ')
for i in range(a-2):
    s=f1+f2
    print(s,end=' ')
    f1=f2
    f2=s
    
