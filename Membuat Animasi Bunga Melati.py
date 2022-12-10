import turtle
import os
os.system('cls')

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#262626')
t.pencolor('magenta')
t.speed(12000)
colors = ('red','yellow','cyan','blue')
for x in range(5):
    for y in range(8):
        t.speed(y + 10)
        for i in range(2):
            t.pensize(2)
            t.circle(60+x*12,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(colors[x%4])
s.exitonclick()