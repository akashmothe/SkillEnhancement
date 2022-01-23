# Write a Python program to count the frequency of words in a file.

f = open("space.txt", 'r')
data = f.read().split(' ')
words_count = {}
for word in data:
    words_count[word] = data.count(word)

print(words_count)
f.close()