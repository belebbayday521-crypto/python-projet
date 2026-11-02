
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        c = a + b
        a = b
        b = c

    return a

print(fibonacci(10))
print(fibonacci(10000))