import sqlite3
import tkinter as tk
con=sqlite3.connect(r"C:\Users\Student\Desktop\form1.db")
cur=con.cursor()
cur.execute("create table  if not exists student(ID text primary key,Name text,LastName text,Web text ,Network text,programming text,Age text)")

def checklist(i,o,p):
    global a,b,c
    a="وب" if i==1 else ""
    b="شبکه" if o==1 else ""
    c="برنامه نویسی" if p==1 else""
    return (i,o,p)




def imp():

    x=var1.get()
    y=var2.get()
    z=var3.get()
    d=var4.get()
    q=checklist(x,y,z)
    dsp=tk.Label(root,text=ed1.get()+"\n"+ed2.get()+"\n"+ed3.get()+"\n"+a+"\n"+b+"\n"+c+"\n"+d,font=("b nazanin",20,"bold"),fg="blue",bg="white",width=30)
    dsp.place(x=600,y=600)

    t1=[ed1.get(),ed2.get(),ed3.get(),a,b,c,d]
    cur.execute("insert into student values(?,?,?,?,?,?,?)",t1)
    con.commit()


def dell():  
    y=[]
    cur.execute("SELECT * from student ")        
    o = cur.fetchall()
    z=ed1.get()
    for i in o:
        y.append(i[0])
    if z in y:
        z=[ed1.get()]
        cur.execute("DELETE  FROM student WHERE ID=? ",z)
        dsp2=tk.Label(root,text='deleted',fg='green',bg='#dcd5d0',font=('B nazanin',20,'bold'))
        dsp2.place(x=300 , y=350)
        con.commit()
    else:
        dsp2=tk.Label(root,text='dont exits this ID',fg='red',bg='#dcd5d0',font=('B nazanin',20,'bold'))
        dsp2.place(x=300 , y=350)





root=tk.Tk()
root.geometry("800x800")
root.configure(bg="black",highlightcolor="magenta",highlightthickness=3,bd=3)
root.title("form")



lbl1=tk.Label(text="کد ملی",font=("b nazanin",20,"bold"),fg="pink",bg="black")
lbl1.grid(row=1,column=0)
ed1=tk.Entry(font=("b nazanin",20,"bold"),width=40)
ed1.grid(row=1,column=2)


lbl2=tk.Label(text="نام",font=("b nazanin",20,"bold"),fg="pink",bg="black")
lbl2.grid(row=2,column=0)
ed2=tk.Entry(font=("b nazanin",20,"bold"),width=40)
ed2.grid(row=2,column=2)

lbl3=tk.Label(text="نام خانوادگی",font=("b nazanin",20,"bold"),fg="pink",bg="black")
lbl3.grid(row=3,column=0)
ed3=tk.Entry(font=("b nazanin",20,"bold"),width=40)
ed3.grid(row=3,column=2)



lbl4=tk.Label(text="فیلد مورد علاقه",font=("b nazanin",20,"bold"),fg="pink",bg="black")
lbl4.grid(row=4,column=0)

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
ch1=tk.Checkbutton(root,text="وب", variable=var1,fg="pink",bg="black",font=("b nazanin",15,"bold"))
ch1.place(x=100,y=200)
ch2=tk.Checkbutton(root,text="شبکه", variable=var2,fg="pink",bg="black",font=("b nazanin",15,"bold"))
ch2.place(x=200,y=200)
ch3=tk.Checkbutton(root,text="برنامه نویسی", variable=var3,fg="pink",bg="black",font=("b nazanin",15,"bold"))
ch3.place(x=300,y=200)




lbl5=tk.Label(text="سن خود را وارد نماید",font=("b nazanin",20,"bold"),fg="pink",bg="black")
lbl5.place(x=0,y=250)


var4=tk.StringVar()
var4.set("20-30")
r1=tk.Radiobutton(root,text="age 20-30",variable=var4,value="20-30",font=("b nazanin",15,"bold"),fg="pink",bg="black")
r1.place(x=100,y=300)

r2=tk.Radiobutton(root,text="age 20-30",variable=var4,value="30-40",font=("b nazanin",15,"bold"),fg="pink",bg="black")
r2.place(x=300,y=300)

r3=tk.Radiobutton(root,text="age 20-30",variable=var4,value="40-50",font=("b nazanin",15,"bold"),fg="pink",bg="black")
r3.place(x=500,y=300)



reg=tk.Button(root,text="import",font=("b nazanin",15,"bold"),fg="pink",bg="black",command=imp)
reg.place(x=100, y=550)

clear=tk.Button(root,text="clear",font=("b nazanin",15,"bold"),fg="pink",bg="black",command=dell)
clear.place(x=200, y=550)

tk.mainloop()
