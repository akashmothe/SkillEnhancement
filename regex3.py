# Write a Python program that matches a word at the beginning of a string

import re

# def start_with(txt):
#     pattern = "\AThe"
#     if re.search(pattern, txt):
#         print("Found")
#     else:
#         print("Not found")


# start_with("The sky")
# start_with("sky")
# start_with("sky The")


# Write a Python program that matches a word at the end of string, with optional punctuation.

def ends_with(txt):
    pattern = "akash\Z"
    if re.search(pattern, txt):
        print("Found")
    else:
        print("Not found")

ends_with("Hi akash")