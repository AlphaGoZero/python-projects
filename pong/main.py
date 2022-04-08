from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

moving_speed = 0.1
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(moving_speed)

    # detect whether that ball hit the wall or not
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect whether the ball contact the paddle and bounce
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # speed up the game every paddle bounce
        if moving_speed >= 0.02:
            moving_speed *= 0.9
    # left player scores
    if ball.xcor() > 380:
        scoreboard.left_score += 1
        scoreboard.update()
        ball.reset()
    # right player scores
    if ball.xcor() < -380:
        scoreboard.right_score += 1
        scoreboard.update()
        ball.reset()
