import sqlite3
conn=sqlite3.connect(r"C:\Users\Student\Desktop\database1.db")
x=conn.cursor()
list1=[]
for i in range(3):
    id=input("enter your ID")
    name=input("enter your name")
    lastname=input("enter your lastname")
    age=int(input("enter your age"))
    address=input("enter your address")
    average=float(input("enter your average"))
    list1.append((id,name,lastname,age,address,average))
x.executemany("insert into user values(?,?,?,?,?,?)",list1)
conn.commit()
conn.close()
