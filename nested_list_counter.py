# Write a Python program to get the frequency of the elements in a given list of lists. Use collections module.

from collections import Counter
l = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
new_list = []
for i in l:
    for j in i:
        new_list.append(j)

print(Counter(new_list))
