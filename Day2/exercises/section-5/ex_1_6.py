from collections import OrderedDict

def ordered_dict_iteration():
    od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
    return list(od.items())

ordered_items = ordered_dict_iteration()
print(ordered_items)  # Output: [('a', 1), ('b', 2), ('c', 3)]
