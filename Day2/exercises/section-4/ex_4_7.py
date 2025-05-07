import itertools


def group_by_key():
    data = [{"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 30},
            {"name": "David", "age": 25}]

    # Sort the data by age to use groupby effectively
    sorted_data = sorted(data, key=lambda x: x["age"])
    return itertools.groupby(sorted_data, key=lambda x: x["age"])


grouped = group_by_key()
for key, group in grouped:
    print(f"Age {key}: {list(group)}")
