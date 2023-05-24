"""Kata - Is this a triangle?

completed at: 2023-05-22 19:55:40
by: Jakub Červinka

Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

"""

def is_triangle(*args):
    a, b, c = sorted(args)
    return (a + b) > c
