from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.5)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scores.score_update()

    #Detect collision to wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scores.game_over()

    #Detect collision with tail
    for each_seg in snake.segments[1:]:
         if snake.head.distance(each_seg) < 10:
            game_is_on = False
            scores.game_over()


s.exitonclick()
