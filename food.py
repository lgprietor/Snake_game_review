import turtle as t
import random

class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.new_food = t.Turtle()
        self.new_food.penup()
        self.new_food.speed("fastest")
        self.new_food.shape("circle")
        self.new_food.color("blue")
        self.new_food.shapesize(0.5)

        self.change_location()

    def change_location(self):

        new_x = random.randint(-270,270)
        new_y = random.randint(-270, 270)

        self.new_food.goto(x=new_x, y=new_y)






