from collections import deque

def stack_and_queue_operations():
    stack = deque()
    queue = deque()

    # Simulating a stack (LIFO)
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack_pop = stack.pop()  # Output: 3

    # Simulating a queue (FIFO)
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue_pop = queue.popleft()  # Output: 1

    return stack_pop, queue_pop

stack_pop, queue_pop = stack_and_queue_operations()
print(stack_pop, queue_pop)  # Output: 3 1
