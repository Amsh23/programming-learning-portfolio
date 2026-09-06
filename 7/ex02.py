import  tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
def calc():
    try:
        num1=float(ent1.get())
        num2=float(ent2.get())
        o=op.get()
        if o=="+":
            result=num1+num2
        elif o=="-":
            result=num1-num2
        elif o=="*":
            result=num1*num2
        elif o=="/":
            if num2==0:
                messagebox.showerror("خطا","تقسیم بر صفر اشتباه است")
            result=num1/num2
        resultlbl.config(text=f"result={result}")
    except ValueError:
        resultlbl.config(text="لطفا عدد وارد کن")

master=tk.Tk()
master.title("محاسبه چهار عمل اصلی")
master.geometry("500x500")
master.config(bg="silver",borderwidth=7,highlightcolor="#B34EF2",highlightthickness=10)
lbl1=tk.Label(master,text="عدد اول را وارد کنید",font=("b nazanin",15,"bold"),fg="#B34EF2",bg="silver")
lbl1.pack(pady=10)
ent1=tk.Entry(font=("b nazanin",15,"bold"),width=30)
ent1.pack(pady=10)
#flat, groove, raised, ridge, solid, or sunken
lbl2=tk.Label(master,text="عدد دوم را وارد کنید",font=("b nazanin",15,"bold"),fg="#B34EF2",bg="silver", relief="flat")
lbl2.pack(pady=10)
ent2=tk.Entry(font=("b nazanin",15,"bold"),width=30)
ent2.pack(pady=10)
op=Combobox(master,values=["+","-","*","/"],font=("b nazanin",15,"bold"))
op.current(3)
op.pack(pady=10)
resultlbl=tk.Label(master,text="نتیجه",font=("b nazanin",15,"bold"),fg="#B34EF2",bg="silver", relief="flat")
resultlbl.pack(pady=10)
btn=tk.Button(master,text="محاسبه",font=("b nazanin",15,"bold"),fg="#B34EF2",bg="silver",command=calc)
btn.pack(pady=10)
master.mainloop()