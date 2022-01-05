import numpy as np

class Sand:
    def __init__(self, width, height):
        # 2d array of x,y
        self.sand = np.zeros(shape=(width, height))
        self.width = width
        self.height = height

    def add_sand_circle(self, center_x, center_y, radius):
        points_in_circle = self.get_points_in_circle(center_x, center_y, radius)
        for point in points_in_circle:
            self.add_sand_pixel(point[0], point[1])

    def add_sand_pixel(self, x, y):
        self.sand[x][y] = 1

    def get_points_in_circle(self, center_x, center_y, radius):
        ret = []

        # bounding box
        min_x = center_x - radius
        max_x = center_x + radius
        min_y = center_y - radius
        max_y = center_y + radius

        center = np.array((center_x, center_y))

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                point = np.array((x, y))
                if abs(np.linalg.norm(point - center)) <= radius:
                    # condition is sand-specific
                    if 0 <= x < self.width and 0 <= y < self.height:
                        ret.append((x, y))

        return ret

