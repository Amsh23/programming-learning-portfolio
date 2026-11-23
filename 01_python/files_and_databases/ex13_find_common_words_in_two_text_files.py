# f1=open(r"C:\Users\Student\Desktop\test.txt","r")
# f2=open(r"C:\Users\Student\Desktop\t.txt","r")
# print(set(f1.read().split())& set(f2.read().split()))




f1=open(r"C:\Users\Student\Desktop\test.txt","r")
f2=open(r"C:\Users\Student\Desktop\t.txt","r")
x=f1.read().split()
y=f2.read().split()
for i in x:
    if i in y:
        print(i)