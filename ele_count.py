# Write a Python program to count the occurrence of each element of a given list.

from collections import Counter
l = ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
print(Counter(l))

l2 = [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
print(Counter(l2))
