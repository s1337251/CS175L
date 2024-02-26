#CS175L
#Jimmy Kong
#stopsign.py

#turtle program
import math
import turtle

#variable list
window_width = 400
window_height = 400
animation_speed = 0
num_sides = 8
length = 100
angle = 45
text_x = 5
text_y = -10

#diameter of octagon = 241.42
#radius of octagon = 120.71

screen = turtle.Screen()
screen.setup(window_width, window_height)

turtle.shape('turtle')
turtle.hideturtle()
turtle.speed(animation_speed)

turtle.penup()
turtle.goto(-60,120)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()

for i in range(num_sides):
    turtle.forward(length)
    turtle.right(angle)

turtle.end_fill()

turtle.penup()
turtle.goto(-55,110)
turtle.pendown()
turtle.color('white')
turtle.width(7.5)

for i in range(num_sides):
    turtle.forward(90)
    turtle.right(angle)

turtle.hideturtle()

turtle.penup()
turtle.right(-75)
turtle.forward(-150)
turtle.color('white')
turtle.write('STOP', font=('Arial', 50, 'normal'))

turtle.done()