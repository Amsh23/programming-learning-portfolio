# list1=[1,2,3,4,5,6,7,8,9,10]
# print(list1)



# list1=[]

# for i in range(1,11):
#     list1.append(i)
# print(list1)


# print([i*10 for i in range(1,11) if i%2==0])

# print(dir(set))

print([i for i in dir(set) if not i.startswith("__")])