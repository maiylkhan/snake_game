from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

user_name = screen.textinput("Hi!","Enter your name: ")
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        score.increase_score()
        snake.increase_speed()
        food.refresh()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        score.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
