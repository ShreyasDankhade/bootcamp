import itertools

def repeat_pattern():
    return itertools.cycle(["red", "green", "blue"])

pattern_gen = repeat_pattern()
for _ in range(6):
    print(next(pattern_gen))  # Output: red, green, blue, red, green, blue
