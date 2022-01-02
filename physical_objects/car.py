CAR_WIDTH = 25
CAR_HEIGHT = 10
ROTATION_INCREMENT_DEG = 15
MOVEMENT_INCREMENT = 5
SENSOR_DISTANCE = 15
SENSOR_RADIUS = 4

class Car:
    def __init__(self, position_x, position_y):
        # position is the center of the front of the car
        self.position_x = position_x
        self.position_y = position_y
        # angle between y-axis and front of car
        self.angle_deg = 0
