'''Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the
 creation and print the members of the dictionary in reverse order.'''

from collections import OrderedDict

d = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
new_dict = OrderedDict(d.items())
for i in new_dict:
    print(i, new_dict[i])

print("Reversed Dict")
for key in reversed(new_dict):
    print(key, new_dict[key])   