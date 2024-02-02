import turtle as t
from snake import Snake
import time

screen = t.Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=600,canvheight=600)
screen.listen()

snake = Snake()

game_is_on = True

while game_is_on:
    time.sleep(1)
    snake.move_snake()







screen.exitonclick()