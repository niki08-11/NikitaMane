# Example: calculate factorial of 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}")
print(f"The factorial of {n} is {result}")
