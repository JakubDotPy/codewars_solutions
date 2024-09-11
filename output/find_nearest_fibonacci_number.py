"""Kata - Find Nearest Fibonacci Number

completed at: 2024-09-10 10:51:31
by: Jakub Červinka

Given a positive integer (n) find the nearest fibonacci number to (n). 

If there are more than one fibonacci with equal distance to the given number return the smallest one.

Do it in a efficient way. 5000 tests with the input range 1 <= n <= 2^512 should not exceed 200 ms.

"""

def nearest_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    a_num, num_b = number - a, b - number
    return a if a_num <= num_b else b
    
