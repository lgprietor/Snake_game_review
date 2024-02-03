import turtle as t
from snake import Snake
import time

screen = t.Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=600,canvheight=600)
screen.listen()

snake = Snake()

screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    snake.move_snake()

    # Moving right












screen.exitonclick()