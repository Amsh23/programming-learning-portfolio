import turtle
turtle.title("hello")
turtle.pensize(3)
turtle.pencolor("silver")
turtle.fillcolor("cyan")
#turtle.shape("turtle")
#turtle square circle arrow classic
turtle.ht()
turtle.speed("slow")
turtle.penup()
turtle.goto(-300,200)
turtle.pendown()
turtle.write("welcome",font=("times new roman",12,"bold"))
turtle.begin_fill()
for i in range(3):
    turtle.forward(150)
    turtle.right(120)
turtle.end_fill()
turtle.done()