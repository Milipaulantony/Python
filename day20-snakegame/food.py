from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5,0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_co_or = random.randint(-280, 280)
        y_co_or = random.randint(-280, 280)
        self.goto(x_co_or, y_co_or)