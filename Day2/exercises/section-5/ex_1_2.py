from collections import Counter

def count_characters(text):
    return Counter(text)

text = "hello world"
char_count = count_characters(text)
print(char_count)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
