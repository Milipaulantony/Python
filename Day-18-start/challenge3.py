from turtle import Turtle,Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

directions = [0, 90, 180, 270]

color_choice = ["cyan", "DarkRed", "chartreuse", "DarkViolet", "DeepPink", "aquamarine2","DarkOrange","DarkGoldenrod"]

for _ in range(200):
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random.choice(color_choice))

this_screen = Screen()
this_screen.exitonclick()