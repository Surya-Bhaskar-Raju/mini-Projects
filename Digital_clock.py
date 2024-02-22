import turtle
import time
import datetime as dt


s=turtle.Turtle()
t=turtle.Turtle()
c=turtle.Turtle()


screen=turtle.Screen()
screen.bgcolor("white")

sec=dt.datetime.now().second
min=dt.datetime.now().minute
hr=dt.datetime.now().hour

#Drawing the circle

c.penup()
c.goto(0,-150)
c.pendown()
c.color("#9E2931")
c.begin_fill()
c.circle(150)
c.end_fill()
c.hideturtle()

#Drawing the rectangle

t.pensize(3)
t.color('white')
t.penup()
t.goto(-100,-35)
t.pendown()
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(70)
    t.left(90)
t.hideturtle()

#Accessing curent time using datetime module

s.goto(-90,-30)
s.color("white")
while True:
    s.hideturtle()
    s.clear()
    s.write(str(hr).zfill(2)+":"+str(min).zfill(2)+":"+str(sec).zfill(2),font=("Times new roman",37,'bold'))
    time.sleep(1)
    sec+=1
    if sec==60:
        min+=1
        sec=0
    if min==60:
        hr+=1
        min=0
    if hr==13:
        hr=1
        
        
turtle.mainloop()
