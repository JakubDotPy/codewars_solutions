"""Kata - Fundamentals: Return

completed at: 2024-03-12 14:57:16
by: Jakub Červinka

Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.

Please use the following function names:

```if-not:csharp
addition = **add**

multiply = **multiply**

division = **divide** (both integer and float divisions are accepted)

modulus = **mod**

exponential = **exponent**

subtraction = **subt**
```

```if:csharp
addition = **Add**

multiply = **Multiply**

division = **Divide** 

modulus = **Mod**

exponential = **Exponent**

subtraction = **Subt**

**Note: All funcitons can return int and all will recieve 2 integers.** 
```


*Note: All math operations will be:
  a (operation) b*

"""

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

def mod(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def subt(a, b):
    return a - b
