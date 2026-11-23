# f=open(r"C:\Users\Student\Desktop\test.txt","r")
# for i in f.read().split():
#     if i[0]=="p" or i[0]=="P":
#         print(i)





# f=open(r"C:\Users\Student\Desktop\test.txt","r")
# for i in f.read().split():
#     if i.startswith("p") or i.startswith("P"):
#         print(i)




f=open(r"C:\Users\Student\Desktop\test.txt","r")
for i in f.read().split():
    if i.startswith("p" or "P"):
        print(i)
