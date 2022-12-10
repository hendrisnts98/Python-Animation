import turtle

turtle.bgcolor('black')
turtle.speed(80)
turtle.hideturtle()

colors = ["white", "salmon", "pink", "red"]

for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(180-i, 100)
        turtle.lt(90)
        turtle.circle(180-i, 100)
        turtle.end_fill()

turtle.mainloop()