import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('hirstpic.png', 30)

list_colors = [ (color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors ]
screen = Screen()
screen.colormode(255)

arrow = Turtle()
arrow.shape('arrow')
arrow.pensize(4)

def dashed_line(obj):
    obj.pendown()
    for _ in range(10):
        rand_col = random.choice(list_colors)
        obj.pencolor(rand_col)
        obj.dot()
        obj.penup()
        obj.forward(20)

arrow.speed('fastest')
for row in range(10):
    dashed_line(arrow)
    arrow.setpos(0, arrow.ycor()+20)

screen.exitonclick()