"""Kata - Make a function that does arithmetic!

completed at: 2023-06-17 13:53:38
by: Jakub Červinka

Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them. 


```a``` and ```b``` will both be positive integers, and ```a``` will always be the first number in the operation, and ```b``` always the second.

The four operators are "add", "subtract", "divide", "multiply". 

~~~if-not:haskell
A few **examples:(Input1, Input2, Input3 --> Output)**
```
5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5
```
~~~

~~~if:haskell
In **Haskell**:

  1. The operation is defined as
```haskell
data Operation = Add | Divide | Multiply | Subtract deriving (Eq, Show, Enum, Bounded)
```
  2. The arithmetic function as 
```haskell
arithmetic :: Double -> Double -> Operation -> Double
arithmetic :: Fractional a => a -> a -> Operation -> a
```
~~~


Try to do it without using if statements!

"""

from operator import add
from operator import sub
from operator import mul
from operator import truediv

def arithmetic(a, b, op):
    op_to_op = {
        'add': add,
        'subtract': sub,
        'multiply': mul,
        'divide': truediv,
    }
    return op_to_op[op](a, b)
