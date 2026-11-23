import tkinter as tk
class mean_calculate:
    def __init__(self,master):
        self.master=master
        master.title(" محاسبه ی معدل")
        master.configure(bg="silver")
        self.label=tk.Label(master,text="نمره ی آزمون اول",font=("b nazanin",14,"bold"),fg="blue",bg="silver")
        self.label.place(x=300,y=100)
        self.entry1=tk.Entry(master,font=("b nazanin",14,"bold"),width=20)
        self.entry1.place(x=300,y=150)
        self.labe2=tk.Label(master,text="نمره ی آزمون دوم",font=("b nazanin",14,"bold"),fg="blue",bg="silver")
        self.labe2.place(x=300,y=200)
        self.entry2=tk.Entry(master,font=("b nazanin",14,"bold"),width=20)
        self.entry2.place(x=300,y=250)
        self.calculate_button=tk.Button(master,text="محاسبه ی معدل",font=("b nazanin",10,"bold"),width=15,height=2,command=self.calculate_gpa)
        self.calculate_button.place(x=300,y=300)
        self.result=tk.Label(master,text="",font=("b nazanin",14,"bold"),fg="red",bg="blue")
        self.result.place(x=300,y=400)
    def calculate_gpa(self):
        try:
            grade1=float(self.entry1.get())
            grade2=float(self.entry2.get())
            c=(grade1+grade2)/2
            self.result.config(text=f"معدل شما={c}")
        except ValueError:
            self.result.config(text="لطفا عدد وارد کنید")
root=tk.Tk()
calculate_gpa=mean_calculate(root)
root.mainloop()