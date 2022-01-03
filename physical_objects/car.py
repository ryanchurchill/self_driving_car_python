import math

class Car:
    CAR_WIDTH = 25
    CAR_HEIGHT = 10
    ROTATION_INCREMENT_DEG = 15
    MOVEMENT_INCREMENT = 5
    SENSOR_DISTANCE = 15
    SENSOR_RADIUS = 4

    def __init__(self, position_x, position_y):
        # position is the center of the front of the car
        self.position_x = position_x
        self.position_y = position_y
        # angle between y-axis and front of car
        self.angle_deg = 0

    def moveForward(self):
        # straight left movement vector, assuming angle of 0
        movement_vector = (-self.MOVEMENT_INCREMENT, 0)

        # rotate
        movement_vector = self.rotateVectorClockwise(movement_vector, self.angle_deg)
        print(movement_vector)

        self.position_x = self.position_x + movement_vector[0]
        self.position_y = self.position_y + movement_vector[1]

    def rotateLeft(self):
        self.setAngleDeg(self.angle_deg - self.ROTATION_INCREMENT_DEG)

    def rotateRight(self):
        self.setAngleDeg(self.angle_deg + self.ROTATION_INCREMENT_DEG)

    def setAngleDeg(self, angle_deg):
        self.angle_deg = angle_deg
        if (self.angle_deg < 0):
            self.angle_deg += 360
        if (self.angle_deg >= 360):
            self.angle_deg -= 360

    def rotateVectorClockwise(self, point, angle_deg):
        angle_rad = math.radians(angle_deg)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        x = point[0] * cos_a + point[1] * sin_a
        y = point[0] * sin_a + point[1] * cos_a

        return x, y