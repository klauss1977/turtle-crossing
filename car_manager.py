from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_cars()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for _ in range(random.randint(0, 8)):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(random.randint(100, 280), random.randint(-250, 280))
            self.all_cars.append(new_car)

    def move(self):
        for car in range(len(self.all_cars)):
            new_x = self.all_cars[car].xcor() - self.move_speed
            new_y = self.all_cars[car].ycor()
            self.all_cars[car].goto(new_x, new_y)
        if self.all_cars[len(self.all_cars) - 1].xcor() < 0:
            self.create_cars()

    def destroy_car(self):
        for car in self.all_cars:
            if car.xcor() < -280:
                car.clear()
                self.all_cars.remove(car)
                car.hideturtle()

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
