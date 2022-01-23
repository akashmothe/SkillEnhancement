#  Write a Python program to get the file size of a plain file

import os
file_size = os.path.getsize("space.txt")
print(f"File size is: {file_size} bytes")