def countdown(n):
    while n > 0:
        yield n
        n -= 1

def simple_generator():
    for count in countdown(5):
        print(count)

simple_generator()