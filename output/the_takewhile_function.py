"""Kata - The takeWhile Function

completed at: 2024-07-16 19:18:10
by: Jakub Červinka

Here's another staple for the functional programmer. You have a sequence of values and some predicate for those values. You want to get the longest prefix of elements such that the predicate is true for each element. We'll call this the `takeWhile` function. It accepts two arguments. The first is the sequence of values, and the second is the predicate function. The function does not change the value of the original sequence.

### Example:

```
sequence : [2,4,6,8,1,2,5,4,3,2]
predicate: is an even number
result   : [2,4,6,8]
```

Your task is to implement the takeWhile function. 

If you've got a [span function](http://www.codewars.com/kata/the-span-function) lying around, this is a one-liner! Also, if you liked this problem, you'll surely love [the dropWhile function](http://www.codewars.com/kata/the-dropwhile-function).

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` and deconstructor `foldl` for your `List` encoding  
export constructors `False, True` for your `Boolean` encoding  
~~~
"""

from itertools import takewhile

def take_while(iterable, fn):
    return list(takewhile(fn, iterable))
