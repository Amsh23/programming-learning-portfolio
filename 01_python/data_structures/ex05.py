list1=input("enter=").split()
print(list1)
dict1={}
for i in list1:
    dict1[i[0]]=int(i[1:])
    # dict1.update({i[0]:int(i[1:])})
print(sum(dict1.values()))
print(max(dict1.values()))
print(min(dict1.values()))