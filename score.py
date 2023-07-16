from turtle import Turtle
from main import ball, r_paddle, l_paddle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super.__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("silver")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score is: Left: {self.l_score} Right: {self.r_score}")

    def increment_score(self):
        if ball.distance(r_paddle) > 100 and ball.xcor() > 350:
            self.l_score += 1
            self.clear()
            self.update_scoreboard()
        elif ball.distance(l_paddle) > 100 and ball.xcor() < -350:
            self.r_score += 1
            self.clear()
            self.update_scoreboard()

    def game_over(self):
        if self.l_score >= 10:
            self.clear()
            self.write(f"GAME OVER: Left player wins. \n Final score: {self.l_score} for player left {self.r_score} "
                       f"points for player right.")
        elif self.r_score >= 10:
            self.clear()
            self.write(f"GAME OVER: Right player wins. \n Final score: {self.r_score} for player right, {self.l_score}"
                       f"points for player left.")