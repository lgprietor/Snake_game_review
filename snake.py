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
            new_turtle = t.Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.speed("slowest")
            new_turtle.goto(x=-20*i, y=0)
            self.snake_parts.append(new_turtle)

    def move_snake(self):

        for part in self.snake_parts:
            position = part.position()
            self.snake_positions.append(position)

        # print(self.snake_positions)

        for i in range(1,len(self.snake_parts)):

            self.snake_parts[i].goto(self.snake_positions[i-1])

        self.snake_head.forward(20)

        self.snake_positions = []

    def move_up(self):

        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def move_down(self):

        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def move_right(self):

        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def move_left(self):

        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)






