from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("silver")
        self.penup()
        self.goto(-80, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score is: Left: {self.l_score} Right: {self.r_score}", align=ALIGNMENT, font=FONT)

    def increment_score_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increment_score_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.l_score >= 5:
            self.clear()
            self.goto(0, 0)
            self.write(f"GAME OVER: \n Left player wins. \n Final score: {self.l_score} for player left {self.r_score} "
                       f"points for player right.", align=ALIGNMENT, font=FONT)
        elif self.r_score >= 5:
            self.clear()
            self.goto(0, 0)
            self.write(f"GAME OVER: Right player wins. \n Final score: {self.r_score} for player right, {self.l_score}"
                       f"points for player left.", align=ALIGNMENT, font=FONT)
