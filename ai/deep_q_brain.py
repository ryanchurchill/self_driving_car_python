import random
from physical_objects.car import Car
from physical_objects.car_move import CarMove
from physical_objects.sand import Sand
from physical_objects.sensor_type import SensorType
from util.math_util import MathUtil
from util.point import Point
from ai.network import Network

# Input States:
# 0 => Orientation
# 1 => SensorType.LEFT
# 2 => SensorType.MIDDLE
# 3 => SensorType.RIGHT
#
# Output Actions:
# 0 => CarMove.LEFT
# 1 => CarMove.FORWARD
# 2 => CarMove.RIGHT
#
# Rewards:
# "The tough card": Bad reward is stronger than good reward
# - Driving into sand:              -1
# - Too close to borders:           -1
# - Moving away from destination:   -.2
# - Moving toward destination:      +.1

class DeepQBrain:
    def __init__(self, car: Car, sand: Sand, goals: list[Point]):
        self.car = car
        self.sand = sand
        self.goals: list = goals
        self.current_goal: Point = self.goals[0]

        self.network = Network(4, 3)

    def decide_next_move(self, signal_left: float, signal_forward: float, signal_right: float):
        print('Input states..')
        print('Orientation: ' + str(self.calculate_orientation()))
        print('Left Signal: ' + str(signal_left))
        print('Middle Signal: ' + str(signal_forward))
        print('Right Signal: ' + str(signal_right))

    def calculate_orientation(self):
        car_to_goal_vector = Point(self.current_goal.x - self.car.position_x, self.current_goal.y - self.car.position_y)
        car_position_vector = self.car.getSensorVector(SensorType.MIDDLE)
        return MathUtil.rotation_between_vectors_deg(car_position_vector, car_to_goal_vector)


