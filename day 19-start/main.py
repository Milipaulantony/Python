from turtle import Turtle, Screen
import random

is_race_on = False
s = Screen()
s.setup(width=500, height=400)
user_choice = s.textinput(title="Make bet", prompt="Which color would win?: ").lower()
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []

# def move_forward():
#     tim.forward(50)
# def move_backward():
#     tim.backward(50)
# def move_counter_clk():
#     #tim.circle(120,-50)
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
# def move_clock():
#     #tim.circle(120,50)
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# s.listen()
# s.onkey(move_forward, "w")
# s.onkey(move_backward, "s")
# s.onkey(move_counter_clk, "a")
# s.onkey(move_clock,"d")
# s.onkey(clear_screen,"c")

x = -230
y = -150

for color_type in colors:
    t = Turtle(shape="turtle")
    t.color(color_type)
    t.penup()
    t.goto(x, y)
    y += 50
    all_turtles.append(t)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle_obj in all_turtles:
        if turtle_obj.xcor() < 230:
            distance_to_move = random.randint(1,10)
            turtle_obj.forward(distance_to_move)
        else:
            is_race_on = False
            winning_color = turtle_obj.pencolor()
            if user_choice == winning_color:
                print(f"You win.The winning color is {winning_color}")
            else:
                print(f"You lose. The winning color is {winning_color}")

s.exitonclick()