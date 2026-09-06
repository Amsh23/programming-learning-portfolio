import turtle
turtle.title("hello")
turtle.pensize(3)
screen=turtle.Screen()
screen.tracer(0)
turtle.ht()
color=["silver","#D457F2","cyan","orange","pink"]
r=20
for i in range(10):
    turtle.pencolor(color[i%5])
    turtle.circle(r,steps=200)
    r+=5


screen.update()

turtle.done()