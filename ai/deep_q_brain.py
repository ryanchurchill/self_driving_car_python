import random
from physical_objects.car import Car
from physical_objects.car_move import CarMove
from physical_objects.sand import Sand

# Input States:
# 0 => Orientation
# 1 => signal_1
# 2 => signal_2
# 3 => signal_3
#
# Output Actions:
# 0 => Forward
# 1 => Turn Left
# 2 => Turn Right
#
# Rewards:
# "The tough card": Bad reward is stronger than good reward
# - Driving into sand:              -1
# - Too close to borders:           -1
# - Moving away from destination:   -.2
# - Moving toward destination:      +.1

class DeepQBrain:
    def __init__(self, car: Car, sand: Sand):
        self.car = Car
        self.sand = Sand

    def decide_next_move(self):
        return random.choice(list(CarMove))

    # def make_next_move(self, move:CarMove):
    #     next_move = self.get_next_move()
    #     self.game_widget.car.makeMove(next_move)

