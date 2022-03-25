import math
from util.point import Point
import numpy as np

class MathUtil:
    @staticmethod
    def rotate_vector_clockwise(point: Point, angle_deg):
        angle_rad = math.radians(angle_deg)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        x = point.x * cos_a + point.y * sin_a
        y = point.x * sin_a + point.y * cos_a

        return Point(x, y)

    @staticmethod
    def angle_between_vectors_deg(v1: Point, v2: Point) -> float:
        vector_1 = v1.get_list()
        unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
        vector_2 = v2.get_list()
        unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
        dot_product = np.dot(unit_vector_1, unit_vector_2)
        angle_radians = np.arccos(dot_product)
        return math.degrees(angle_radians)

    # how much to rotate v1 to make it point in the same direction as v2
    # positive number means rotate clockwise (right)
    # negative number means rotate counter-clockwise (left)
    @staticmethod
    def rotation_between_vectors_deg(v1: Point, v2: Point) -> float:
        vector_1 = v1.get_list()
        unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
        vector_2 = v2.get_list()
        unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
        dot_product = np.dot(unit_vector_1, unit_vector_2)
        angle_radians = np.arccos(dot_product)
        angle_deg = math.degrees(angle_radians)

        c = np.cross(vector_2, vector_1)
        if c > 0:
            angle_deg *= -1

        return angle_deg