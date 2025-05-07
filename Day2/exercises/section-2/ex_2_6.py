def check_chained_comparison(x):
    if 0 < x < 10:
        return "x is between 0 and 10"
    else:
        return "x is out of range"


result = check_chained_comparison(5)
print(result)
