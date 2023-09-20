# Find the factorial of a given number (n!)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# Find out the n'th number in fibonacci series
def fibonacci(n):
    if n <= 0:
        return "Error!"
    elif n == 1 or n == 2:
        return n-1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("Factorial of n = ", factorial(5))
    print("N'th value in a Fibonacci series = ", fibonacci(10))
