names = ["flower","flow","floor"]
prefix = names[0]
for words in names:
    while not words.startswith(prefix):
        prefix = prefix[::-1]
print(prefix)
