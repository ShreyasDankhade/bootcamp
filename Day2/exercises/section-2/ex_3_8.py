def conditional_in_comprehension():
    return ['even' if x % 2 == 0 else 'odd' for x in range(5)]

result = conditional_in_comprehension()
print(result)
# Output: ['even', 'odd', 'even', 'odd', 'even']
