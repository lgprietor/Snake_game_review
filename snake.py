import turtle as t

INITIAl_SIZE = 3


class Snake(t.Turtle):

    def __init__(self):
        super().__init__()
        self.snake_parts = []
        self.snake_body()

    def snake_body(self):

        for i in range(INITIAl_SIZE):
            new_turtle = Snake()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(x = 20*i, y = 0)
            self.snake_parts.append(new_turtle)


        # self.goto(x=-20*i, y=0)
        # self.snake_parts.append(new_turtle)
