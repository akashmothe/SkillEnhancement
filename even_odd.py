numbers = [i for i in range(1,10)]
even = []
odd = []
for i in numbers:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Odd Numbers: {odd}")
print(f"Even Numbers: {even}")  