# Write a Python program to group a sequence of key-value pairs into a dictionary of lists

d = {'a':1, 'b':['a','e','i','o','u'], 'c':234, 'd':"Akash"}
res = []
for key in d.items():
    res.append(key)
print(res)