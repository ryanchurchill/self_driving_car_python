class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def get_list(self) -> list:
        return self.x, self.y
