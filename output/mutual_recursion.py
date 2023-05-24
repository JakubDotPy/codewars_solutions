"""Kata - Mutual Recursion

completed at: 2023-05-04 07:27:49
by: Jakub Červinka

Mutual Recursion allows us to take the fun of regular recursion (where a function calls itself until a terminating condition) and apply it to multiple functions calling each other! 

Let's use the Hofstadter Female and Male sequences to demonstrate this technique. You'll want to create two functions `F` and `M` such that the following equations are true: 

```
F(0) = 1
M(0) = 0
F(n) = n - M(F(n - 1))
M(n) = n - F(M(n - 1))
```

Don't worry about negative numbers, `n` will always be greater than or equal to zero.

~~~if:php,csharp
You *do* have to worry about performance though, mutual recursion uses up a lot of stack space (and is highly inefficient) so you may have to find a way to make your solution consume less stack space (and time).  Good luck :)
~~~

~~~if:lambdacalc
- Purity: `Let`
- Number Encoding: `Scott`
~~~

Hofstadter Wikipedia Reference http://en.wikipedia.org/wiki/Hofstadter_sequence#Hofstadter_Female_and_Male_sequences

"""

from functools import cache

@cache
def f(n):
    if n == 0:
        return 1
    elif n >0:
        return n - m(f(n-1))

@cache
def m(n):
    if n==0:
        return 0
    elif n >0:
        return n - f(m(n-1))
