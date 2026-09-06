list1=input("enter=").split()
print(list1)
dict1={}
for i in list1:
    # dict1[i[0]]=i[1:]
    dict1.update({i[0]:i[1:]})
print(dict1)