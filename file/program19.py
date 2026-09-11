a = [("a", 1), ("b", 2), ("c", 3)]
res = dict(map(lambda x: (x[0], x[1]), a))
print(res)