import turtle 
import random 
import time 
def goto(a,b): 
    turtle.penup() 
    turtle.goto(a,b) 
    turtle.pendown()       
def rectangle(a,c,e,f): 
    goto(e,f) 
    turtle.fillcolor("black") 
    turtle.begin_fill() 
    for i in range(2): 
        turtle.forward(a) 
        turtle.right(90) 
        turtle.forward(c) 
        turtle.right(90) 
    turtle.end_fill() 
         
you = system = 0 
my_list = ["rock","paper","scissors"] 
turtle.pencolor("cyan") 
turtle.shape("arrow")
turtle.ht() 
turtle.speed("fast") 
turtle.pensize(5) 
turtle.bgcolor("black") 
turtle.title("ROCK PAPAER SCISSORS") 
 
rectangle(650,100,-320,310) 
goto(0,240) 
turtle.write("  ROCK  PAPAER  SCISSORS  ",align='center',font=("tahoma",30,"bold")) 
 
rectangle(325,40,-320,200) 
goto(-160,165) 
turtle.write("SYSTEM",align='center',font=("tahoma",20)) 
rectangle(325,40,5,200) 
goto(165,165) 
turtle.write("YOU",align='center',font=("tahoma",20)) 
rectangle(325,60,-320,150) 
goto(-160,105) 
turtle.write(system,align='center',font=("tahoma",20)) 
rectangle(325,60,5,150) 
goto(165,105) 
turtle.write(you,align='center',font=("tahoma",20)) 
 
while True: 
    rectangle(325,380,-320,80) 
    rectangle(325,380,5,80) 
    vorodi = turtle.textinput("R P S","PLEASEN ENTER : R = ROCK , P = PAPER , S = SCISSORS " ) 
    if vorodi.lower() == "r": 
        goto(170,-190) 
        turtle.circle(100) 
    elif vorodi.lower() == "p": 
        rectangle(150,180,100,0) 
    elif vorodi.lower() == "s": 
        goto(200,-100) 
        turtle.circle(20) 
        turtle.left(10) 
        turtle.backward(140) 
        goto(200,-160) 
        turtle.circle(20) 
        goto(200,-122) 
        turtle.right(30) 
        turtle.backward(140) 
    turtle.penup()     
    turtle.home() 
    turtle.pendown()    
    rand = random.choice(my_list) 
    if rand == "rock": 
        goto(-150,-190) 
        turtle.circle(100) 
    elif rand == "paper": 
        rectangle(150,180,-220,0) 
    elif rand == "scissors": 
        goto(-200,-100) 
        turtle.circle(20) 
        turtle.right(10) 
        turtle.forward(140) 
        goto(-200,-160) 
        turtle.circle(20) 
        goto(-200,-120) 
        turtle.left(20) 
        turtle.forward(140)    
    turtle.penup()     
    turtle.home() 
    turtle.pendown()  
 
    ra,v,r,p,s = rand[0] , vorodi.lower(), "r" , "p" , "s" 
    if ra == v: 
        pass 
    elif ra == r and v == s: 
        system = system + 1 
    elif ra == r and v == p: 
        you = you + 1 
    elif ra == p and v == r: 
        system = system + 1 
    elif ra == p and v == s: 
        you = you + 1 
    elif ra == s and v == p: 
        system = system + 1 
    elif ra == s and v == r: 
        you = you + 1 
    else: 
        pass 
 
    rectangle(325,60,-320,150) 
    goto(-160,105) 
    turtle.write(system,align='center',font=("tahoma",20)) 
    rectangle(325,60,5,150) 
    goto(165,105) 
    turtle.write(you,align='center',font=("tahoma",20)) 
     
    time.sleep(3) 
turtle.done()