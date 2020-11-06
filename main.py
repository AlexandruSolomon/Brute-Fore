def factorial(n):
    if n == 1:
        return n

    else:
        return n * factorial(n - 1)


x = 2
print(x + 3)
output = []

for k in range(x):
    output.append(max(k, x))

out = factorial(1)
print(out)