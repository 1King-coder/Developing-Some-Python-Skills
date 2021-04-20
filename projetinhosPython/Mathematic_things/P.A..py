from functools import reduce

pa = [60, 70, 89, -2, 140, 1, -8]
print(reduce(lambda x, y: x if x > y else y, pa))
