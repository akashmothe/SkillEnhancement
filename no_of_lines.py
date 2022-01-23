# Write a Python program to count the number of lines in a text file

f = open("space.txt", "r")
print(len(f.readlines()))
f.close()