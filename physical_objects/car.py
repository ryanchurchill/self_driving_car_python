import math

from physical_objects.car_move import CarMove
from physical_objects.sensor_type import SensorType
from util.point import Point
from util.math_util import MathUtil

class Car:
    CAR_WIDTH = 25
    CAR_HEIGHT = 10
    ROTATION_INCREMENT_DEG = 20
    DEFAULT_SPEED = 6
    SAND_SPEED = 1
    SENSOR_DISTANCE = 15
    SENSOR_RADIUS = 4

    def __init__(self, position_x: int, position_y: int, game_width: int, game_height: int):
        # position is the center of the front of the car
        self.position_x: float = position_x
        self.position_y: float = position_y
        self.game_width = game_width
        self.game_height = game_height
        # angle between x-axis and front of car - 0 means facing left
        self.angle_deg: int = 0

        self.speed = self.DEFAULT_SPEED

        # storage of past events
        self.last_rotation: CarMove

    def __moveForward(self):
        # straight left movement vector, assuming angle of 0
        movement_vector = Point(-self.speed, 0)

        # rotate
        movement_vector = MathUtil.rotate_vector_clockwise(movement_vector, self.angle_deg)
        # print(movement_vector)

        new_x = self.position_x + movement_vector.x
        new_y = self.position_y + movement_vector.y

        # if self.is_position_out_of_bounds(Point(new_x, new_y)):
        #     return

        self.position_x = new_x
        self.position_y = new_y

    def __rotateLeft(self):
        self.setAngleDeg(self.angle_deg - self.ROTATION_INCREMENT_DEG)

    def __rotateRight(self):
        self.setAngleDeg(self.angle_deg + self.ROTATION_INCREMENT_DEG)

    def makeMove(self, move: CarMove):
        if move == CarMove.LEFT:
            self.__rotateLeft()
        elif move == CarMove.RIGHT:
            self.__rotateRight()
        elif move == CarMove.FORWARD:
            self.__moveForward()
        else:
            print('Error!! makeMove for invalid CarMove')

    def setAngleDeg(self, angle_deg):
        self.angle_deg = angle_deg
        if (self.angle_deg < 0):
            self.angle_deg += 360
        if (self.angle_deg >= 360):
            self.angle_deg -= 360

    # center of the circle
    def getSensorCoordinates(self, sensor_type: SensorType) -> Point:
        sensor_vector = self.getSensorVector(sensor_type)
        return Point(self.position_x + sensor_vector.x, self.position_y + sensor_vector.y)

    def getSensorVector(self, sensor_type: SensorType) -> Point:
        # straight line pointing left
        sensor_vector = Point(-self.SENSOR_DISTANCE, 0)

        additional_angle_deg = 0
        if sensor_type == SensorType.LEFT:
            additional_angle_deg = -45
        elif sensor_type == SensorType.RIGHT:
            additional_angle_deg = 45

        return MathUtil.rotate_vector_clockwise(sensor_vector, (self.angle_deg + additional_angle_deg))

    def is_position_out_of_bounds(self, point: Point) -> bool:
        return point.x < 0 or \
            point.x > self.game_width or \
            point.y < 0 or \
            point.y > self.game_height






