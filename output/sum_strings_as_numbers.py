"""Kata - Sum Strings as Numbers

completed at: 2024-09-21 20:48:27
by: Jakub Červinka

Given the string representations of two integers, return the string representation of the sum of those integers.

For example:
```javascript
sumStrings('1','2') // => '3'
```
```c
strsum("1", "2")    /* => 3 */
```

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of `BigInteger` and `BigDecimal` in java

Python:
your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""

from itertools import zip_longest

def adder_gen(x, y):
    carry = 0
    for x, y in zip_longest(x, y, fillvalue=0):
        n = x + y + carry
        carry, res = divmod(n, 10)    
        yield res
    yield carry
    
def sum_strings(x, y):    
    remap = lambda s: map(int, s[::-1])
    carry = 0
    x_nums, y_nums = remap(x), remap(y)
    gen = adder_gen(x_nums, y_nums)
    result_s = ''.join(str(n) for n in gen)[::-1]
    
    if result_s in ('0', '00'):
        return '0'
    
    return result_s.lstrip('0')

