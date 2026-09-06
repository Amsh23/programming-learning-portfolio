import turtle
import random
turtle.title("hello")
turtle.pensize(3)
turtle.ht()
color=["silver","#D457F2","cyan","orange","pink"]
r=20
for i in range(10):
    turtle.pencolor(random.choice(color))
    turtle.circle(r)
    r+=5
turtle.done()