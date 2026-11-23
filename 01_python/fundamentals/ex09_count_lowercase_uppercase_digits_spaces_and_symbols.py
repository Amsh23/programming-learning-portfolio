str1=input("enter string=")
l=u=d=s=sp=0
for i in  str1:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
    else:
        sp+=1
print(f"lower={l}-upper={u}-space={s}-digit={d}-special char={sp}")
