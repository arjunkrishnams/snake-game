from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0)
snake=Snake()
score=Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.update()

food=Food()
while(1):
 
    time.sleep(0.1)
    screen.update()
    snake.move()
    new_x=snake.head.xcor()
    new_y=snake.head.ycor()
    if(snake.head.distance(food) < 15):
        food.refresh()
        score.update()
        segment= Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(snake.x,snake.y)
        snake.segments.append(segment)

        
    if(new_x>290 or new_x <-290 or new_y >290 or new_y<-290):
        score.reset()
        snake.reset()
    

    for element in snake.segments[1:]:
        x=element.xcor()
        y=element.ycor()
        if(x==new_x and y==new_y):
            score.reset()
            snake.reset()
            break


score.game_over()
screen.exitonclick()