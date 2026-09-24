# import colorgram
#
# colors = colorgram.extract('hirst_spot.jpg', 15)
#
# list_of_colors = []
# for color_obj in colors:
#     r = color_obj.rgb.r
#     g = color_obj.rgb.g
#     b = color_obj.rgb.b
#     list_of_colors.append((r, g, b))
#
# print(list_of_colors)

import turtle as t
import random

color_list = [(196, 174, 118), (158, 104, 60), (124, 37, 24), (182, 155, 53), (8, 56, 81), (111, 67, 82), (47, 36, 32), (116, 161, 174), (26, 121, 168), (76, 37, 46), (11, 65, 46)]
t.colormode(255)
tim = t.Turtle()

# tim.dot(20,random.choice(color_list))
# tim.forward(50)
# tim.dot(20,random.choice(color_list))
#tim.goto(0,-250)
# print(tim.pos())

tim.penup()
y_co_ord = -250
for column_count in range(10):
    x_co_ord = -250
    for row_count in range(10):
        tim.goto(x_co_ord, y_co_ord)
        tim.dot(20, random.choice(color_list))
        x_co_ord += 50

    y_co_ord += 50

my_screen = t.Screen()
my_screen.exitonclick()