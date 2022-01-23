# Write a Python program to make a chain of function decorators in Python.

def main_func(fn):
    def inner():
        fn()
    return inner


def used_func():
    print("This is used_func.")

main_func(used_func())