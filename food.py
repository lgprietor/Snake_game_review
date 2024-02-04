import turtle as t
import random


class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5)
        self.refresh_location()

    def refresh_location(self):
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 270)

        self.goto(x=new_x, y=new_y)
