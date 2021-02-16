from turtle import Screen, Turtle, shape
import random


# def move_forwards():
#     tim.forward(10)

# def clockwise():
#     tim.right(5)

# def c_clockwise():
#     tim.left(5)

# def backwards():
#     tim.backward(10)

# def clear_s():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


# for _ in range(20):
#     screen.listen()
#     screen.onkey(key="w", fun=move_forwards)
#     screen.onkey(key="s", fun=backwards)
#     screen.onkey(key="a", fun=c_clockwise)
#     screen.onkey(key="d", fun=clockwise)
#     screen.onkey(key="c", fun=clear_s)

is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="make your bet", prompt="which turtle will win?")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                print('winner')
            else:
                print('you did not win!')
            
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()