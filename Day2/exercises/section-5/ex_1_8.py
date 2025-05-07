from collections import defaultdict

def nested_defaultdict():
    d = defaultdict(lambda: defaultdict(int))
    d["group1"]["member1"] = 5
    d["group1"]["member2"] = 3
    d["group2"]["member1"] = 2
    return dict(d)

nested_dict = nested_defaultdict()
print(nested_dict)  # Output: {'group1': defaultdict(<class 'int'>, {'member1': 5, 'member2': 3}),
                    #          'group2': defaultdict(<class 'int'>, {'member1': 2})}
