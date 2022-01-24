import re
# Write a Python program that matches a string that has an a followed by zero or more b's.

# def starts_end_with(text):
#     pattern = "^a(b*)$"
#     if re.search(pattern, text):
#         print("Found")
#     else:
#         print("Not found")

# starts_end_with("ab")
# starts_end_with("asdf")
# starts_end_with("a")
# starts_end_with("abbb")


# Write a Python program that matches a string that has an a followed by one or more b's.

# def starts_end_with(text):
#     pattern = "^a(b+)$"
#     if re.search(pattern, text):
#         print("Found")
#     else:
#         print("Not found")

# starts_end_with("a")
# starts_end_with("ab")
# starts_end_with("abbb")



# Write a Python program that matches a string that has an a followed by zero or one 'b'.

# def starts_end_with(text):
#     pattern = "^a(b?)$"
#     if re.search(pattern, text):
#         print("Found")
#     else:
#         print("Not found")

# starts_end_with("a")
# starts_end_with("ab")
# starts_end_with("adk")
# starts_end_with("abbb")



# Write a Python program that matches a string that has an a followed by three 'b'

# def starts_end_with(text):
#     pattern = '^ab{3}?'
#     if re.search(pattern, text):
#         print("Found")
#     else:
#         print("Not found")

# starts_end_with("abb")
# starts_end_with("abbb")
# starts_end_with("a")
# starts_end_with("abbbbbc")


# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'


def starts_end_with(text):
    pattern = '^a.+?b$'
    if re.search(pattern, text):
        print("Found")
    else:
        print("Not found")

starts_end_with("akasb")
starts_end_with("ab")
starts_end_with("a")
starts_end_with("b")