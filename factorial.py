#!/usr/bin/python3
import sys

def factorial(n):
    result = 1 
    while n > 1:
        result *= n
        n -= 1  # 👈 هذا هو التعديل المهم
    return result

f = factorial(int(sys.argv[1]))
print(f)
