import random
from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)   # Reduces the intensity at which cars are created.Cars created only if randint picks '1'.
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.penup()
            car_color = random.choice(COLORS)
            new_car.color(car_color)
            Y_AXIS = random.randint(-260, 260)
            new_car.goto(280, Y_AXIS)
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        # MOVE_INCREMENT =
        for car in self.all_cars:
            car.backward(self.car_speed)






