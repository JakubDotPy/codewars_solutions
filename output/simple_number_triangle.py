"""Kata - Simple number triangle

completed at: 2024-07-08 23:52:59
by: Jakub Červinka

Consider the number triangle below, in which each number is equal to the number above plus the number to the left. If there is no number above, assume it's a `0`.

```haskell
1
1 1
1 2 2
1 3 5 5
1 4 9 14 14
```
The triangle has `5` rows and the sum of the last row is `sum([1,4,9,14,14]) = 42`.

You will be given an integer `n` and your task will be to return the sum of the last row of a triangle of `n` rows. 

In the example above:
```haskell
solve(5) = 42
```
More examples in test cases. Good luck!

```if:javascript
### Note

This kata uses native arbitrary precision integer numbers ( `BigInt`, `1n` ).  
Unfortunately, the testing framework and even native `JSON` do not fully support them yet.  
`console.log(1n)` and `(1n).toString()` work and can be used for debugging.  

We apologise for the inconvenience.
```
"""

from math import factorial

def solve(n):
    return factorial(2 * n) // (factorial(n) * factorial(n+1))
