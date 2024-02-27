import turtle as t

FONT = ("Courier", 18, "normal")
class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        with open("data.txt") as file:
            contents = file.read()
            self.highscore = int(contents)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(x=-130,y=270)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)
        self.goto(x=100, y=270)
        self.write(arg=f"Highscore: {self.highscore}", move=False, align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(x=-130, y=270)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)
        self.goto(x=100, y=270)
        self.write(arg=f"Highscore: {self.highscore}", move=False, align="center", font=FONT)

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="Game over", move=False, align="center", font=FONT)

    def reset_board(self):

        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.goto(x=-130, y=270)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)
        self.goto(x=100, y=270)
        self.write(arg=f"Highscore: {self.highscore}", move=False, align="center", font=FONT)


