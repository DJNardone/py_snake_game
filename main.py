from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Classic")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_in_play = True
while game_in_play:
    screen.update()  # turns off the turtle animation and updates screen
    time.sleep(0.1)  # at a set interval, using the time.sleep module.
    snake.move()
    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.new_food()
        score.keep_score()
        snake.extend_snake()
    # detect collision with wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or \
            snake.snake_head.ycor() < -290:
        score.reset()
        snake.reset()
    # detect collision with tail
    for segment in snake.snake_parts[1:]:
        if snake.snake_head.distance(segment) < 5:
            score.reset()
            snake.reset()


screen.exitonclick()