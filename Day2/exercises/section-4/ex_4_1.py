import itertools

def generate_ids():
    return itertools.count(1)  # Starts generating from 1

id_gen = generate_ids()
for _ in range(5):
    print(next(id_gen))  # Output: 1, 2, 3, 4, 5
