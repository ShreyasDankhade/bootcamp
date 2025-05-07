from collections import defaultdict

def group_words_by_first_letter(words):
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)
    return grouped

words = ["apple", "banana", "apricot", "blueberry", "cherry"]
grouped_words = group_words_by_first_letter(words)
print(dict(grouped_words))  # Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
