'''Write a Python program to check the validity of password input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.'''

import re 
password = input("Enter your password: ")

while True:
    if (len(password) < 6) or (len(password) > 16):
    	print("Password length should be in between 6 to 16")
        break
    elif not re.search("[a-z]",password):
    	print("Your password don't have small alphabates.")
        break
    elif not re.search("[A-Z]",password):
        print("Your password don't have capital alphabates.")
        break
    elif not re.search("[0-9]", password):
        print("Please include atleast one number.")
        break
    elif not re.search("[$#@]", password):
        print("Please include atleast one special character")
        break
    else: 
    	print("Great..!! Your password is valid.")
        break