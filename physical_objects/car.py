import math

from physical_objects.car_move import CarMove
from physical_objects.sensor_type import SensorType


class Car:
    CAR_WIDTH = 25
    CAR_HEIGHT = 10
    ROTATION_INCREMENT_DEG = 20
    DEFAULT_SPEED = 6
    SAND_SPEED = 1
    SENSOR_DISTANCE = 15
    SENSOR_RADIUS = 4

    def __init__(self, position_x: int, position_y: int):
        # position is the center of the front of the car
        self.position_x: float = position_x
        self.position_y: float = position_y
        # angle between x-axis and front of car - 0 means facing left
        self.angle_deg: int = 0

        self.speed = self.DEFAULT_SPEED

        # storage of past events
        self.last_rotation: CarMove

    def __moveForward(self):
        # straight left movement vector, assuming angle of 0
        movement_vector = (-self.speed, 0)

        # rotate
        movement_vector = self.rotateVectorClockwise(movement_vector, self.angle_deg)
        # print(movement_vector)

        self.position_x = self.position_x + movement_vector[0]
        self.position_y = self.position_y + movement_vector[1]

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

    def setAngleDeg(self, angle_deg):
        self.angle_deg = angle_deg
        if (self.angle_deg < 0):
            self.angle_deg += 360
        if (self.angle_deg >= 360):
            self.angle_deg -= 360

    # center of the circle
    def getSensorCoordinates(self, sensor_type: SensorType):
        # straight line pointing left
        sensor_vector = (-self.SENSOR_DISTANCE, 0)

        additional_angle_deg = 0
        if sensor_type == SensorType.LEFT:
            additional_angle_deg = -45
        elif sensor_type == SensorType.RIGHT:
            additional_angle_deg = 45

        sensor_vector = self.rotateVectorClockwise(sensor_vector, self.angle_deg + additional_angle_deg)

        return (self.position_x + sensor_vector[0], self.position_y + sensor_vector[1])

    def rotateVectorClockwise(self, point, angle_deg):
        angle_rad = math.radians(angle_deg)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        x = point[0] * cos_a + point[1] * sin_a
        y = point[0] * sin_a + point[1] * cos_a

        return x, y





