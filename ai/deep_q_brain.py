from physical_objects.car import Car
from physical_objects.car_move import CarMove
from physical_objects.sand import Sand
from physical_objects.sensor_type import SensorType
from util.math_util import MathUtil
from util.point import Point
from ai.dqn import Dqn
import numpy as np

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

        self.dqn_brain = Dqn(4, 3, 0.9)

        self.last_distance = -1

    def decide_next_move(self, signal_left: float, signal_forward: float, signal_right: float, is_car_on_sand: bool, is_car_out_of_bounds: bool):
        current_state = [self.calculate_orientation(), signal_left, signal_forward, signal_right]
        current_distance = self.calculate_distance()
        current_reward = self.calculate_reward(current_distance, is_car_on_sand, is_car_out_of_bounds)
        next_action = self.dqn_brain.update(current_state, current_reward)

        self.last_distance = current_distance

        # print(int(next_action))
        # return next_action

        print('Input states..')
        print('Orientation: ' + str(self.calculate_orientation()))
        print('Left Signal: ' + str(signal_left))
        print('Middle Signal: ' + str(signal_forward))
        print('Right Signal: ' + str(signal_right))
        print('Current Distance: ' + str(current_distance))
        print('Current Reward: ' + str(current_reward))

        return CarMove(int(next_action))

    def calculate_orientation(self):
        car_to_goal_vector = Point(self.current_goal.x - self.car.position_x, self.current_goal.y - self.car.position_y)
        car_position_vector = self.car.getSensorVector(SensorType.MIDDLE)
        return MathUtil.rotation_between_vectors_deg(car_position_vector, car_to_goal_vector)

    def calculate_distance(self):
        return np.sqrt((self.car.position_x - self.current_goal.x)**2 + (self.car.position_y - self.current_goal.y)**2)

    def calculate_reward(self, current_distance, is_car_on_sand, is_car_out_of_bounds) -> float:
        if self.last_distance == -1:
            return 0
        if is_car_on_sand or is_car_out_of_bounds:
            return -1
        if current_distance < self.last_distance:
            return .1
        return -.2


