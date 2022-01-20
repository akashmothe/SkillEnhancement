# Write a Python function to multiply all the numbers in a list.
def multiply_nums(l):
    res = 1
    for i in l:
        res *= i
    return res

l = [8, 2, 3, -1, 7]
print(multiply_nums(l))