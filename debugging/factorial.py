#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if len(sys.argv) != 2:
    print("Usage: python script.py <non-negative integer>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    print(factorial(num))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

