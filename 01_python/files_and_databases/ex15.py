# import csv
# from statistics import mean
# list2=[]
# f=open(r"c:\Users\Student\Desktop\file01.csv","r")
# w=open(r"c:\Users\Student\Desktop\file02.csv","w")
# x=csv.reader(f)
# y=csv.writer(w)
# header=next(x)
# header.append("average")
# y.writerow(header)
# for i in x:
#     name=i[0]
#     list1=[]
#     for j in i[1:]:
#         list1.append(float(j))
#     average=mean(list1)
#     i.append(average)
#     y.writerow(i)
#     print(f"average of {name} is {mean(list1):0.2f}")
# f.close()
# w.close()






import csv
from statistics import mean
list2=[]
f=open(r"c:\Users\Student\Desktop\file01.csv","r")
x=csv.reader(f)
list1=[]
for i in x:
    name=i[0]
    for j in i[1:]:
        list1.append(float(j))
print(round(mean(list1),2))   
