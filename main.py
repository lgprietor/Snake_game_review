import turtle as t
from snake import Snake
from food import Food
import time


screen = t.Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=600,canvheight=600)
screen.listen()

snake = Snake()
food = Food()

screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    snake.move_snake()

    # Detecting collisions with the food:

    # food_x = food.xcor()
    # food_y = food.ycor()

    # print(snake.snake_head.distance()

    print(snake.snake_head.distance(food.position()))

    if snake.snake_head.distance(food.position()) < 15:
        food.change_location()





        # food.change_location()













screen.exitonclick()