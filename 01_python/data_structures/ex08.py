list1=input("enter=").split()
print(list1)
dict1={}
for i in list1:
    dict1[i[0]]=int(i[1:])
print(dict1)


list1=input("enter=").split()
print(list1)
dict2={}
for i in list1:
    dict2[i[0]]=int(i[1:])
print(dict2)

dict3={}
for i in dict1.keys():
    if i in dict2.keys():
        dict3.update({i:dict1[i]+dict2[i]})
        print(i,dict1[i]+dict2[i])
print(dict3)