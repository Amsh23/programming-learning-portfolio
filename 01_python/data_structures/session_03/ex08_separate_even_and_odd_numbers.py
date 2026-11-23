list1=input("enter a number=").split()
print(list1)
even,odd=[],[]
for i in list1:
    if int(i)%2==0:
        even.append(int(i))
    else:
        odd.append(int(i))
print(f"even={even},odd={odd}")