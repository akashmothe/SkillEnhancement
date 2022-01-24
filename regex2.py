# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

# def find_match(txt):
#     pattern = "^[a-z]+_[a-z]+$"
#     if re.search(pattern, txt):
#         print("Found")
#     else:
#         print("Not found")


# find_match("akash_mothe")
# find_match("akash_mothE")
# find_match("akash__mothe")
# find_match("akash_")
# find_match("akash_ak_mothe")


# Write a Python program to find the sequences of one upper case letter followed by lower case letters

def find_match(txt):
    pattern = "^[A-Z][a-z]+$"
    if re.search(pattern, txt):
        print("Found")
    else:
        print("Not found")


find_match("Akash")
find_match("akash")
find_match("akAsh")