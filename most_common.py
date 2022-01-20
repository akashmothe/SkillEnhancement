# Write a Python program to find the most common elements and their counts of a specified text.

from collections import Counter

string = input("Enter the string: ")

print(Counter(string).most_common(3))

