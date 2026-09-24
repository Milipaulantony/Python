import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

print(tim.heading())

tim.setheading(tim.heading() + 5)
print(tim.heading())import turtle as t
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


for _ in range(30):
    timmy_the_turtle.circle(100)
    timmy_the_turtle.right(12)
    timmy_the_turtle.color(random_color())

this_screen = t.Screen()
this_screen.bgcolor("orange")
this_screen.exitonclick()
