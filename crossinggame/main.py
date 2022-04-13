import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_num = random.choice([x for x in range(6)])
    if random_num == 0:
        car_manager.make_random_car()
    car_manager.move_car()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            scoreboard.lose()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.win()
        car_manager.level_up()
        player.reset_turtle()

screen.exitonclick()
