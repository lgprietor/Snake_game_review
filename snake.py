import turtle as t

INITIAL_SIZE = 3


class Snake(t.Turtle):

    def __init__(self):
        super().__init__()
        self.snake_parts = []
        self.snake_positions = []
        self.snake_body()
        self.snake_head = self.snake_parts[0]

    def snake_body(self):

        for i in range(INITIAL_SIZE):
            new_part = t.Turtle()
            new_part.color("white")
            new_part.shape("square")
            new_part.penup()
            # Each turtle moves 20 paces because that's the default size of turtle
            new_part.goto(x=-20 * i, y=0)
            self.snake_parts.append(new_part)

    def move_snake(self):

        # Capturing positions:

        for part in self.snake_parts:
            position = part.position()
            self.snake_positions.append(position)

        # Moving each part of snake body excepting snake head:

        for i in range(1, len(self.snake_parts), 1):
            self.snake_parts[i].goto(self.snake_positions[i - 1])

        # Moving the head:

        self.snake_head.forward(20)

        # Resetting the list of positions

        self.snake_positions = []

    def move_up(self):

        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def move_down(self):

        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def move_left(self):

        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def move_right(self):

        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
