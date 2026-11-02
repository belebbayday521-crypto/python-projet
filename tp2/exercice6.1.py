
def fibonacci_recursif(n):
    if n < 2:
        return n

    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

print(fibonacci_recursif(20))
print(fibonacci_recursif(25))
print(fibonacci_recursif(30))