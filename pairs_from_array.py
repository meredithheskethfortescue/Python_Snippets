# create pairs of consecutive elements in a list
values = [1, 2, 3, 4, 5]
pairs = zip(values, values[1:])

# >>> [(1, 2), (2, 3), (3, 4), (4, 5)]
print(list(pairs))
