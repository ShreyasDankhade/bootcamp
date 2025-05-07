from collections import Counter

def most_common_elements(nums, n):
    return Counter(nums).most_common(n)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
top_2 = most_common_elements(numbers, 2)
print(top_2)  # Output: [(4, 4), (3, 3)]
