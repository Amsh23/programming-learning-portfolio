a=input("enter").split()
print(a)
list1=[]
for i in a:
    list1.append(int(i))
a=set(list1)
print(sum(a),max(a),min(a))