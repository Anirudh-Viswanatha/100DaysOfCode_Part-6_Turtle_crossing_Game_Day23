from turtle import Turtle

FONT = ('Areal', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 40, 'normal'))

    def increase_level(self):
        self.level += 1
        self.update_level()
