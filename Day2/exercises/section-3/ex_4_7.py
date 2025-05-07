from collections import namedtuple

# Invalid field name will be auto-renamed
Point = namedtuple("Point", ["x", "y", "2nd_x", "y!"])

# Example usage:
point = Point(1, 2, 3, 4)
print(point)  # Output: Point(x=1, y=2, _2nd_x=3, _y__2=4)
