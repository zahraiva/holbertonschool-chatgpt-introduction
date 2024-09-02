#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer n.

    The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.
    For example, the factorial of 5 (5!) is 5 * 4 * 3 * 2 * 1 = 120.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the integer n. Returns 1 if n is 0, as 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ensure that a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <non-negative integer>")
    sys.exit(1)

try:
    # Convert the command-line argument to an integer
    num = int(sys.argv[1])
    # Ensure that the input is a non-negative integer
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    # Calculate the factorial and print the result
    f = factorial(num)
    print(f)
except ValueError as e:
    # Handle errors in input conversion or invalid inputs
    print(f"Error: {e}")
    sys.exit(1)

