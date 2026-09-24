import turtle as t
import random

t.colormode(255)
timmy_the_turtle = t.Turtle()
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    result_color = (r, g, b)
    color_list = [r, g, b]
    #return color_list
    #return result_color
    return (r, g, b)


for _ in range(200):
    timmy_the_turtle.forward(15)
    timmy_the_turtle.setheading(random.choice(directions))
    color_result = random_color()
    timmy_the_turtle.color(color_result)
    #timmy_the_turtle.color(random_color())

this_screen = t.Screen()
this_screen.exitonclick()