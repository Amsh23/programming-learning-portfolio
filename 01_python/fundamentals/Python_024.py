n=int(input("enter a number"))
for i in range(-n+1,n):
    if i<0:
        i=-i
    space=" "*i
    star="*"*(2*(n-i)-1)
    print(space+star)
