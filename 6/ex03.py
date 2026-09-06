i=1
while i<=20:
    n=1
    c=0
    while n<=i:
        if i%n==0:
            c=c+1
        n=n+1
    if c==2:
        print(i)
    i=i+1
