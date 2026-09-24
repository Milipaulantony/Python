from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score_val = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score_val}", align=ALIGNMENT, font=FONT)
    def score_update(self):
        self.score_val += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0 ,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

