from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

# detecting collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        score.increase_score()


# detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

#detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
