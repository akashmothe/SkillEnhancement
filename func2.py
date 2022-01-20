# Write a Python program that invoke a given function after specific milliseconds.

from time import sleep

def multiply_nums(l):
    res = 1
    for i in l:
        res *= i
    return res

l = [8, 2, 3, -1, 7]

def delay(fn):
    sleep(3)
    return fn

print(delay(multiply_nums(l)))

