b = [1, 2, 3]

# a = b makes a reference to the same list
a = b
a.append(4)
print("b after a.append:", b)
# b is [1, 2, 3, 4] — because a and b refer to the same list

# a = b[:] makes a shallow copy
b = [1, 2, 3]
c = b[:]
c.append(5)
print("b after c.append:", b)  # [1, 2, 3]
print("c:", c)                  # [1, 2, 3, 5]
