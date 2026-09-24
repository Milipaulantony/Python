import turtle as t
import random

color_list = [(196, 174, 118), (158, 104, 60), (124, 37, 24), (182, 155, 53), (8, 56, 81), (111, 67, 82), (47, 36, 32), (116, 161, 174), (26, 121, 168), (76, 37, 46), (11, 65, 46)]
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

my_screen = t.Screen()
my_screen.exitonclick()