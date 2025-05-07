def running_totals(lst):
    total = 0
    for number in lst:
        total += number
        yield total

def generator_with_state():
    numbers = [1, 2, 3, 4]
    for total in running_totals(numbers):
        print(total)

generator_with_state()
