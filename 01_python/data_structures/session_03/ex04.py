list1=[1,1.2,15,1.5,1,4,5,4,5,4]
# print(list1[-1])
#print(list1[::-1])
# print(list1.count("mft"))
# list1.append("rafiepour")
# list1.insert(0,"zeinab")
# list2=["ali","arash"]
# list1.extend(list2)
# del list1[-1]
# list1.remove("mft")
# print(list1)
# list2=list1.copy()
# print(list2)
# list1.sort()
#list1.reverse()

# print(list1.index(1.5))
#list1.pop()
# list1.clear()
# print(list1)
print("-------------1--------")
a=[1,2,3]
b=a
b[0]=100

print(a)
print(b)


print("-------------2--------")

a=[1,2,3]
b=a.copy()
b[0]=100
print(a)
print(b)


print("-------------2--------")
import copy
a=[[1,2],[3,4]]
b=copy.deepcopy(a)
b[0][0]=100
print(a)
print(b)