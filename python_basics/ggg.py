import sys
l1=[i for i in range(100)]
g=(i for i in range(100))
print(type(g))
print(l1)

def fibonacci(n):
    """
    Generator that generates the Fibonacci sequence up to the nth number.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
for num in fibonacci(10):
    print(num)