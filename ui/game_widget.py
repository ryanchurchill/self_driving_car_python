from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor, QPalette
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

from ai.deep_q_brain import DeepQBrain
from ai.random_brain import RandomBrain
from physical_objects.car import Car
from physical_objects.sand import Sand
from physical_objects.sensor_type import SensorType
from physical_objects.car_move import CarMove
from util.point import Point

import numpy as np

# This class is responsible for:
# initializing the objects and game logic
# drawing the objects
# handling input
# processing the brain

class GameWidget(QWidget):
    SAND_PAINTER_RADIUS = 10

    def __init__(self, game_width, game_height):
        super(GameWidget, self).__init__()
        self.car = Car(50, 50, game_width, game_height)
        self.sand = Sand(game_width, game_height)
        self.game_width = game_width
        self.game_height = game_height

        # sand bitmap
        self.sand_pixmap = QtGui.QPixmap(self.game_width, self.game_height)
        self.sand_pixmap.fill(QColor('black'))

        # make background black
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('black'))
        self.setPalette(palette)

        # ai timer
        self.ai_timer = QTimer()
        self.ai_timer.timeout.connect(self.make_next_brain_move)
        self.random_ai = RandomBrain(self.car, self.sand)
        self.ai = DeepQBrain(self.car, self.sand, [Point(game_width, game_height)])

    # DRAWING
    def paintEvent(self, e):
        # print('paintEvent')
        self.drawSand()
        self.drawCar()
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

    def drawSensor(self, qp: QPainter, center_point: Point, color):
        qp.setPen(QColor(color))
        qp.setBrush(QColor(color))
        qp.drawEllipse(
            center_point.x - self.car.SENSOR_RADIUS,
            center_point.y - self.car.SENSOR_RADIUS,
            self.car.SENSOR_RADIUS * 2,
            self.car.SENSOR_RADIUS * 2)

    def drawSand(self):
        paint = QtGui.QPainter()
        paint.begin(self)
        paint.drawPixmap(0, 0, self.sand_pixmap)
        paint.end()

    def drawOntoSandPixmap(self):
        qp = QPainter(self.sand_pixmap)
        # qp.begin(self)

        color = QColor('yellow')
        qp.setPen(color)
        qp.setBrush(color)

        for y in range(self.sand.height):
            for x in range(self.sand.width):
                if self.sand.sand[x, y] == 1:
                    qp.drawPoint(x, y)

        qp.end()

    # INPUT HANDLING
    def handleKeyPressEvent(self, event):
        # print('Key Pressed: ' + str(event.key()))
        if event.key() == QtCore.Qt.Key_W:
            self.move_car(CarMove.FORWARD)
            #test
            # self.sand.add_sand_circle(700, 200, 30)
        if event.key() == QtCore.Qt.Key_A:
            self.move_car(CarMove.LEFT)
        if event.key() == QtCore.Qt.Key_D:
            self.move_car(CarMove.RIGHT)

    def handleMouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        # todo: this implementation is way too slow
        self.sand.add_sand_circle(event.x(), event.y(), self.SAND_PAINTER_RADIUS)
        self.drawOntoSandPixmap()
        self.repaint()

    def button_pressed(self):

        # print("Clicked!")
        self.car.position_x += 10
        self.game_widget.repaint()

    # CAR HANDLING / SENSING - consider moving these to Car and pass sand to the methods
    def move_car(self, move: CarMove):
        # mess with car if it's on sand
        # this just slows it down, but the tutorial also changes its angle
        if self.is_car_on_sand():
            self.car.speed = Car.SAND_SPEED
        else:
            self.car.speed = Car.DEFAULT_SPEED

        self.car.makeMove(move)
        self.repaint()
        print(move)

    def is_car_on_sand(self) -> bool:
        return self.sand.sand[int(self.car.position_x)][int(self.car.position_y)] > 0

    def is_car_out_of_bounds(self) -> bool:
        return self.car.is_position_out_of_bounds(Point(self.car.position_x, self.car.position_y))


    #normalized to 0->1
    def get_sensor_value(self, sensor_type: SensorType) -> float :
        # int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.

        sensor_position: Point = self.car.getSensorCoordinates(sensor_type)
        return int(np.sum(
            self.sand.sand[int(sensor_position.x)-10:int(sensor_position.x)+10,
            int(sensor_position.y)-10:int(sensor_position.y)+10])
        )/400

    # BRAIN HANDLING

    def make_next_brain_move(self):
        move = self.ai.decide_next_move(
            self.get_sensor_value(SensorType.LEFT),
            self.get_sensor_value(SensorType.MIDDLE),
            self.get_sensor_value(SensorType.RIGHT),
            self.is_car_on_sand(),
            self.is_car_out_of_bounds())
        print(move)

        # move = self.random_ai.decide_next_move()

        self.move_car(move)

