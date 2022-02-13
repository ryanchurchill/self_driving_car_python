import random
from physical_objects.car import Car
from physical_objects.car_move import CarMove
from physical_objects.sand import Sand


class RandomBrain:
    def __init__(self, car: Car, sand: Sand):
        self.car = Car
        self.sand = Sand

    def decide_next_move(self):
        return random.choice(list(CarMove))

    # def make_next_move(self, move:CarMove):
    #     next_move = self.get_next_move()
    #     self.game_widget.car.makeMove(next_move)

