import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    snake.move_snake()

    # Detecting collisions with food:

    if snake.snake_head.distance(food) < 15:
        food.refresh_location()
        scoreboard.update_score()
        snake.add_part()

    # Detecting collisions with walls:

    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or
            snake.snake_head.ycor() < -280):

        game_is_on = False
        scoreboard.game_over()

    # Detecting collisions with body:

    for i in snake.snake_parts[1:]:

        if snake.snake_head.distance(i) < 15:

            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()