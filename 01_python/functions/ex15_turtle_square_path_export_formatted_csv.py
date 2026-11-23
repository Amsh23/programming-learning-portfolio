import turtle as t
import csv
path_data=[]
def func():
    x,y=t.pos()
    path_data.append((f"{x:.2f}",f"{y:0.2f}"))
t.pensize(3)
t.pencolor("lightgreen")
for i in range(4):
    func()
    t.forward(100)
    t.right(90)
print(path_data)
with open(r"C:\Users\Student\Desktop\turtle_path.csv","w") as file:
    writer=csv.writer(file)
    writer.writerow(["X","Y"])
    writer.writerows(path_data)
t.done()