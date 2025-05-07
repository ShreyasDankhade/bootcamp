def calculate_score(marks, total):
    """
    Calculate the score as a percentage.
    """
    return (marks / total) * 100

score = calculate_score(80, 100)
print(score)
