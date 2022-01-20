from errno import EXDEV


code = '''print("Hello Akash")'''

func = """
def sum_of_list(l):
    return sum(l)

l = [1,2,3,4,5]
print(sum_of_list(l))
"""

exec(code)
exec(func)