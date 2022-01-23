# Write a Python program to append text to a file and display the text. 

text = input("Enter the text: ")

f = open("space.txt", 'a')
f.write("\n"+text+"\n")
f = open("space.txt", 'r')
data = f.read()
print(data)
f.close()

