import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, key="Up")
player.move_turtle()
player.is_at_finish()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.cars_of_color()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish():
        player.goto_start()
        car_manager.level_up()
        scoreboard.point()

screen.exitonclick()
