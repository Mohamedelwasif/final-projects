import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(a, b):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

# Example usage
a = Point(0, 0)
b = Point(3, 4)
print(distance(a, b))
