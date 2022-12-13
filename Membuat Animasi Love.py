import turtle as t
from random import randint

t.bgcolor('black')
t.shape('turtle')

def curve():
    for i in range(200):
        t.right(1)
        t.fd(1)

def head():
    t.color('red')
    t.begin_fill()
    t.left(140)
    t.fd(120)
    curve()
    t.left(125)
    curve()
    t.fd(120)
    t.end_fill()

def points(x,y,ancho):
    t.up()
    t.goto(x,y)
    t.down()
    t.dot(ancho)
head()
t.up()
t.goto(150,190)
t.pensize(10)
t.hideturtle()
t.color('red2')
t.down()
t.goto(30, 110)

t.up()
t.goto(-60, 50)
t.down()
t.goto(-115, -5)

for i in range(20):
    x = randint(-10,12)
    y = radint(-150,-5)
    a = randint(2,20)
    points(x,y,a)

t.exitonclick()