import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()
game_is_on = True
screen.listen()
screen.onkeypress(player.move, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.destroy_car()
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()
    if player.ycor() > 280:
        player.respawn()
        score.update_level()
        cars.increase_speed()

screen.exitonclick()
