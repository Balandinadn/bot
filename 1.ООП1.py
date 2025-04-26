import math

class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: 'Point2D') -> float:
        """ """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self) -> str:
        """ """
        return f"x:{self.x} y:{self.y}"
