from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGN = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.writing()

    def score_update(self):
        self.score += 1

    def gameover(self):
        self.goto(0,0)
        self.write(arg="GAMEOVER", move=False, align=ALIGN, font=("Arial", 32, "normal"))
    def writing(self):
        self.clear()
        self.write(arg=f"Score is {self.score}", move=False, align=ALIGN, font=FONT)
