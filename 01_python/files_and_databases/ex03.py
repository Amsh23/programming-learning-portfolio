list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)

list2=[]
for i in range(1,11):
    list2.append(i)
print(list2)


print([i*10 for i in range(1,11) if i%2==0])