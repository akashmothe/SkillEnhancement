# Write a Python program that matches a word containing 'z'
import re

def find_match(txt):
    pattern = "\wz"
    if re.search(pattern, txt):
        print("Found")
    else:
        print("Not found")

find_match("xyzx")
find_match("zdkfj")
find_match("sdfjz")
find_match("asdjfzzzlsadfj")
