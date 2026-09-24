import turtle as t
import random

t.colormode(255)
timmy_the_turtle = t.Turtle()
timmy_the_turtle.pensize(2)
timmy_the_turtle.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def draw_spiro(size_gap):
    for _ in range(int(360 / size_gap)):
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_gap)
        timmy_the_turtle.color(random_color())


this_screen = t.Screen()
this_screen.bgcolor("orange")
this_screen.exitonclick()
