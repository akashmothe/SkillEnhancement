# Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
data = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
res = []

for i in data:
    res.append(sum(list(i)))

print(res)
