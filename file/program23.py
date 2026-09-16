t = [(3, 4, 9), (5, 6, 7)]
tup = (1, 2, 5)
K = 3
s = sorted(t, key=lambda x: abs(x[K-1] - tup[K-1]))
res = s[0]
print(res)