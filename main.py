import colorgram
import turtle as turtle_module
from turtle import Turtle, Screen
import random

"""Color selection"""
turtle_module.colormode(255)
color_list = []

colors = colorgram.extract("the_scream.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)
"""Color selection"""

# User selection #
square_size = 1
user_number = 25
space_between = square_size * 20

# User selection ^^^ #

# screen section #
screen = Screen()
screen.tracer(0)

# screen section ^^^ #

timmy = Turtle()
timmy.shape("square")
timmy.shapesize(square_size)
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
turtle_position_x = user_number * -10
turtle_position_y = user_number * -10
timmy.setposition(turtle_position_x, turtle_position_y)


def squares_left(user_number, space_between):
    for x in range(user_number):
        timmy.color(random.choice(color_list))
        timmy.stamp()
        timmy.forward(space_between)


def square_position_change(space_between):
    global turtle_position_y
    turtle_position_y += space_between
    timmy.setposition(turtle_position_x, turtle_position_y)


def square_grid(user_number, space_between):
    for x in range(user_number):
        squares_left(user_number, space_between)
        square_position_change(space_between)


square_grid(user_number, space_between)


screen.exitonclick()
