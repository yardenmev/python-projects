from turtle import Turtle, Screen
import random

the_turtle = Turtle()

colours = ["aquamarine", "cyan", "sky blue", "dark blue"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        the_turtle.forward(100)
        the_turtle.right(angle)

for shape_side_n in range(3, 11):
    the_turtle.color(random.choice(colours))
    draw_shape(shape_side_n)

Screen = Screen()
Screen.exitonclick()