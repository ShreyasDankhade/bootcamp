def accumulator():
    total = 0
    while True:
        num = yield total
        if num is not None:
            total += num

def send_to_generator():
    gen = accumulator()
    next(gen)  # Start the generator
    print(gen.send(5))
    print(gen.send(3))
    print(gen.send(7))

send_to_generator()
