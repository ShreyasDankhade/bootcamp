from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

# Example usage:
point = Point(1, 2)
print(point)  # Output: Point(x=1, y=2)
print(point.x)  # Output: 1
print(point.y)  # Output: 2
