from turtle import Turtle
import random

the_turtle = Turtle()

colours = ["aquamarine", "cyan", "sky blue", "dark blue", "dark olive green", "dark orchid"]
directions = [0, 90, 180, 270]
the_turtle.pensize(7)
the_turtle.speed(10)

while True:
    the_turtle.color(random.choice(colours))
    the_turtle.setheading(random.choice(directions))
    the_turtle.forward(50)
            



