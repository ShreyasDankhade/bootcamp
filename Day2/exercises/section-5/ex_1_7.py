from collections import defaultdict

def defaultdict_with_lambda():
    d = defaultdict(lambda: "N/A")
    d["a"] = 1
    return d["a"], d["b"]  # 'b' is missing, so default value will be used

value_a, value_b = defaultdict_with_lambda()
print(value_a, value_b)  # Output: 1 N/A
