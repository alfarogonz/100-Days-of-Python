from turtle import Screen, Turtle, color, shape
import time, random

tim = Turtle()

tim.shape('turtle')
tim.color('red')

def draw_square(obj):
    for _ in range(4):
        obj.forward(100)
        obj.right(90)

def dashed_line(obj):
    for _ in range(20):
        obj.forward(5)
        obj.penup() if obj.isdown() else obj.pendown()

def create_sided_shape(sides, obj):
    if 360%sides != 0:
        print(f'can\'t do that, can\'t split {sides} by 360')
        return
    else:
        turn_degree = 360/sides
        for _ in range(sides):
            obj.forward(100)
            obj.right(turn_degree)

def create_shapes(obj, shape_count):
    for num in range(3, shape_count+4):
        r = lambda: random.randint(0,255)
        rand_color = '#%02X%02X%02X' % (r(),r(),r())
        obj.pencolor(rand_color)
        create_sided_shape(num, obj)

def random_walk(obj, walks):

    obj.speed('fast')
    obj.pensize(10)
    obj.hideturtle()

    for _ in range(walks):
        r = lambda: random.randint(0,255)
        rand_color = '#%02X%02X%02X' % (r(),r(),r())
        obj.pencolor(rand_color)
        turn_choices = [90, 180, 270, 360]
        obj.right(random.choice(turn_choices))
        obj.forward(20)

def draw_circles(num, turt):
    facing = 0
    for _ in range(num):
        turt.speed('fastest')
        r = lambda: random.randint(0,255)
        rand_color = '#%02X%02X%02X' % (r(),r(),r())
        turt.color(rand_color)
        turt.setheading(facing)
        turt.circle(80)
        facing += 5


draw_circles(100, tim)

screen = Screen()
screen.exitonclick()