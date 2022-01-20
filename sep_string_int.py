# Write a Python program that accepts a string and calculate the number of digits and letters.
string = input("Enter string: ")
letters = 0
digits = 0
for i in string:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    else:
        pass
print(f"Letters: {letters}\nDigits: {digits}")