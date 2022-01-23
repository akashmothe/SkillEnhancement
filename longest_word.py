# Write a python program to find the longest words.

f = open("space.txt", "r")
data = f.read().split(" ")
words_len = 0
word = ""
for i in data:
    if len(i) > words_len:
        words_len = len(i)
        word = i

print(f"{word}: {words_len}")
f.close()