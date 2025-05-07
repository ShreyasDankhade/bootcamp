class Counter:
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            return self.count
        else:
            raise StopIteration

def custom_iterator():
    counter = Counter(3)
    for count in counter:
        print(count)

custom_iterator()
