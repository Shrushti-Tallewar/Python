from collections import Counter

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
count = Counter(a)

res = [num for num, freq in count.items() if freq > 1]
print(res)