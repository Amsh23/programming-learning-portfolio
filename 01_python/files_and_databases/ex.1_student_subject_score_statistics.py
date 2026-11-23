import statistics
dict1={}
list_name=[]
list_math=[]
list_phys=[]
list_chem=[]
for i in range(1,4):
    a=input(f"enter student name{i}")
    b=input("enter mathematics score")
    c=input("enter physics score")
    d=input("enter chemistry score")
    e=f"[{b},{c},{d}]"
    dict1.update({a:e})
    list_name.append(a)
    list_math.append(int(b))
    list_phys.append(int(c))
    list_chem.append(int(d))
print(dict1)

print("math mean score=",statistics.mean(list_math))
print("phys mean score=",statistics.mean(list_phys))
print("chem mean score=",statistics.mean(list_chem))

print("min score in math:",min(list_math),"by",list_name[list_math.index(min(list_math))])
print("max score in math:",max(list_math),"by",list_name[list_math.index(max(list_math))])

print("min score in phys:",min(list_phys),"by",list_name[list_phys.index(min(list_phys))])
print("max score in phys:",max(list_phys),"by",list_name[list_phys.index(max(list_phys))])

print("min score in chem:",min(list_chem),"by",list_name[list_chem.index(min(list_chem))])
print("max score in chem:",max(list_chem),"by",list_name[list_chem.index(max(list_chem))])




