s={}
c=int(input('ent prod count='))
for i in range(c):
    n=input('ent prod name=')
    q=int(input('ent prod quant='))
    p=float(input('ent prod price='))
    s[n]=[q,p]
minq=100000000
for n in s:
    if s[n][0]<minq:
        minq=s[n][0]
        minp=n
print(f'lowest quantity is for {minp}')
quant=[]
for n in s:
    quant.append(s[n][0])
quant.sort()
snames=[]
for i in quant:
    for n in s:
        if s[n][0]==i:
            snames.append(n)
print('lowest to highest quant is for:')
for i in snames:
    print(i,end='<')
print()
v=0
for n in s:
    v+=s[n][0]*s[n][1]
print(f'total value is {v}')