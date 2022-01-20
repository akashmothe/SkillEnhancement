# Write a Python program to convert a given list of tuples to a list of lists.
data = [(1, 2), (2, 3), (3, 4)]
res = []
for i in data:
    res.append(list(i))

print(res)