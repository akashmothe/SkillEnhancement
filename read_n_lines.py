# Write a Python program to read first n lines of a file.

n = int(input("Enter the number of lines: "))
f = open("space.txt", "r")
for i in range(n):
    line = f.readline()
    print(line)
f.close()