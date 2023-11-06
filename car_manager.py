from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_cars()

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
            new_x = self.all_cars[car].xcor() - STARTING_MOVE_DISTANCE
            new_y = self.all_cars[car].ycor()
            self.all_cars[car].goto(new_x, new_y)
            self.all_cars[car].clear()
            # self.all_cars[car].hideturtle()
            self.all_cars[car].write(self.all_cars[car].ycor())
        if self.all_cars[len(self.all_cars) - 1].xcor() < 0:
            self.create_cars()

    def destroy_car(self):
        for car in self.all_cars:
            if car.xcor() < -280:
                car.clear()
                self.all_cars.remove(car)
                car.hideturtle()

    def y_coord(self):
        y_cor = 1000
        for car in self.all_cars:
            if -10 < car.xcor() < 10:
                y_cor = car.ycor()
        return y_cor
