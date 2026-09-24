from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")

color_choice = ["cyan", "DarkRed", "chartreuse", "DarkViolet", "DeepPink", "aquamarine2","DarkOrange","DarkGoldenrod"]
#timmy_the_turtle.color("blue")
timmy_the_turtle.color(color_choice[0])

print(timmy_the_turtle.pos())
angle_turn = 0
c_no = 0
for i in range(3, 11):
    timmy_the_turtle.color(color_choice[c_no])
    angle_turn = 360 / i
    for _ in range(i):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle_turn)
    c_no += 1


this_screen = Screen()
this_screen.exitonclick()