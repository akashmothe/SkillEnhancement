# Write a Python program to get the Fibonacci series between 0 to 50.
fibo = [0,1]
for i in range(50):
    res = fibo[-1] + fibo[-2]
    fibo.append(res)

print(fibo)