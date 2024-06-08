from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# initializing the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

# Key controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is = True
while game_is:
    screen.update()
    time.sleep(0.1)
    # Moving the snake
    snake.move()

    # Snake collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        game_is = False
        score.reset()
        score.game_over()  

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is = False
            score.reset()
            score.game_over()
   
screen.exitonclick()
