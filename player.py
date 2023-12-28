from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.next_level()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)



    # Detect successful crossing
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False





