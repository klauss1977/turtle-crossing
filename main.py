import time
from turtle import Screen
from player import Player
from car_manager import CarManager

# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
all_cars = CarManager()
game_is_on = True
screen.listen()
screen.onkey(player.move, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    all_cars.move()
    all_cars.destroy_car()
    if player.distance(0, all_cars.y_coord()) < 20:
        game_is_on = False
