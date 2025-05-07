def check_any_all(lst):
    any_negative = any(x < 0 for x in lst)
    all_positive = all(x > 0 for x in lst)
    return any_negative, all_positive


result = check_any_all([1, 2, -3, 4])
print(result)