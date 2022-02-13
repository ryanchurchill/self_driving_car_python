from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor, QPalette
from PyQt5.QtWidgets import *

# from ai.random_brain import RandomBrain
from physical_objects.car import Car
from physical_objects.sand import Sand
from physical_objects.sensor_type import SensorType

class GameWidget(QWidget):
    def __init__(self, car: Car, sand: Sand):
        super(GameWidget, self).__init__()
        self.car = car
        self.sand = sand

        # make background black
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('black'))
        self.setPalette(palette)

        # ai timer
        # TODO: probably doesn't make sense for AI Timer here but event processing in main_window
        # self.ai_timer = QTimer()
        # self.ai = RandomBrain()
        # self.ai_timer.timeout.connect(self.ai.make_next_move)

    def paintEvent(self, e):
        print('paintEvent')
        self.drawCar()
        self.drawSand()
        # pass

    def drawCar(self):
        qp = QPainter()
        qp.begin(self)

        color = QColor('white')
        # TODO: difference between Pen and Brush?
        qp.setPen(color)
        qp.setBrush(color)

        # rotate around center of front (left side) of un-rotated car
        qp.translate(self.car.position_x, self.car.position_y)
        qp.rotate(self.car.angle_deg)
        qp.translate(-self.car.position_x, -self.car.position_y)

        # upper-left of unrotated car
        upper_left_x = self.car.position_x
        upper_left_y = self.car.position_y - (self.car.CAR_HEIGHT / 2)
        qp.drawRect(upper_left_x, upper_left_y, self.car.CAR_WIDTH, self.car.CAR_HEIGHT)
        qp.resetTransform()

        # sensors
        point = self.car.getSensorCoordinates(SensorType.LEFT)
        self.drawSensor(qp, point, 'blue')
        point = self.car.getSensorCoordinates(SensorType.MIDDLE)
        self.drawSensor(qp, point, 'red')
        point = self.car.getSensorCoordinates(SensorType.RIGHT)
        self.drawSensor(qp, point, 'green')

        qp.end()

    def drawSensor(self, qp: QPainter, center_point, color):
        qp.setPen(QColor(color))
        qp.setBrush(QColor(color))
        qp.drawEllipse(
            center_point[0] - self.car.SENSOR_RADIUS,
            center_point[1] - self.car.SENSOR_RADIUS,
            self.car.SENSOR_RADIUS * 2,
            self.car.SENSOR_RADIUS * 2)

    def drawSand(self):
        qp = QPainter()
        qp.begin(self)

        color = QColor('yellow')
        qp.setPen(color)
        qp.setBrush(color)

        for y in range(self.sand.height):
            for x in range(self.sand.width):
                if self.sand.sand[x, y] == 1:
                    qp.drawPoint(x, y)

        qp.end()