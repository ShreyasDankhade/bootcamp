from collections import deque

def rotate_deque():
    d = deque([1, 2, 3, 4, 5])
    d.rotate(2)  # Rotate 2 positions to the right
    return list(d)

rotated = rotate_deque()
print(rotated)  # Output: [4, 5, 1, 2, 3]
