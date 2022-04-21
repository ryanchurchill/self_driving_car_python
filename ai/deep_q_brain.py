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
    def __init__(self, car: Car, sand: Sand):
        self.car = car
        self.sand = sand

        self.dqn_brain = Dqn(4, 3, 0.9)

        self.last_distance = -1
        self.last_action = -1

        self.counter = 0

    def decide_next_move(
            self,
            signal_left: float,
            signal_forward: float,
            signal_right: float,
            is_car_on_sand: bool,
            last_move_wall_collision: bool,
            is_at_goal: bool,
            distance_to_goal: float,
            orientation_to_goal: float
    ):
        #divide orientation_to_goal by 180 to normalize it, I think..
        current_state = [orientation_to_goal/180, signal_left, signal_forward, signal_right]
        last_reward = self.calculate_reward(distance_to_goal, is_car_on_sand, last_move_wall_collision, is_at_goal)

        next_action = CarMove(int(self.dqn_brain.update(current_state, last_reward)))

        self.counter += 1
        print('Move #: ' + str(self.counter))
        print('Last state: ' + str(current_state))
        print('Last reward: ' + str(last_reward))
        print('Next move: ' + str(next_action))
        print('Last Distance: ' + str(distance_to_goal))

        # if (current_reward == -1):
        #     print("-1 reward for action: " + str(self.last_action))

        self.last_distance = distance_to_goal
        self.last_action = next_action

        # print(int(next_action))
        # return next_action

        # print('Input states..')
        # print('Orientation: ' + str(orientation_to_goal))
        # print('Left Signal: ' + str(signal_left))
        # print('Middle Signal: ' + str(signal_forward))
        # print('Right Signal: ' + str(signal_right))
        # print('Current Distance: ' + str(distance_to_goal))
        # print('Current Reward: ' + str(current_reward))



        return next_action

    def calculate_reward(self, current_distance: float, is_car_on_sand: bool, last_move_wall_collision: bool, is_car_at_goal: bool) -> float:
        if self.last_distance == -1:
            return 0
        if is_car_at_goal:
            return .1
        if is_car_on_sand or last_move_wall_collision:
            return -1
        if current_distance < self.last_distance:
            return .1
        return -.2
