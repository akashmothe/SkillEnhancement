# Write a Python program to read last n lines of a file

n = int(input("Enter the number of lines: "))
f = open("space.txt", "r")
lines = f.readlines()
for line in lines[-n:]:
    print(line)

f.close()

