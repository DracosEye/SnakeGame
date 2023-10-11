from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.ht()
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 22, "normal"))

    def end_game(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 22, "normal"))