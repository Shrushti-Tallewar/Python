import heapq

t = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
K = 2
res = heapq.nsmallest(1, t, key=lambda x: abs(x[K-1] - tup[K-1]))[0]
print(res)