from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from score import Score
import random



screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car = CarManager()
score = Score()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()    # Create new cars
    car.move()     # Move  cars

    # Detect turtle collision with the car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()
            # player.write("GAME OVER", align='center', font=('Arial', 40, 'normal'))

    # Detect successful crossing
    if player.is_at_finish_line():
        score.increase_level()
        player.next_level()
        car.level_up()





screen.exitonclick()