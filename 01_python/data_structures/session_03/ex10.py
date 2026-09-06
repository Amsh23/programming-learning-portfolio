# s=0
# list1=input("enter a number=").split()
# for i in list1:
#     s=s+int(i)
# print(s)





list1=input("enter a number=").split()
print(list1)
list2=[]
for i in list1:
    list2.append(int(i))
print(list2)
print(sum(list2))
print(min(list2))
print(max(list2))