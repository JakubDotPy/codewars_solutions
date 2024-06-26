"""Kata - Simple frequency sort

completed at: 2023-06-29 08:10:33
by: Jakub Červinka

In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value. 

```haskell
solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
-- We sort by highest frequency to lowest frequency.
-- If two elements have same frequency, we sort by increasing value.
```
```cpp
solve({2,3,5,3,7,9,5,3,7}) == {3,3,3,5,5,7,7,2,9}
// We sort by highest frequency to lowest frequency.
// If two elements have same frequency, we sort by increasing value.
```
```java
Solution.sortByFrequency(new int[]{2, 3, 5, 3, 7, 9, 5, 3, 7});
// Returns {3, 3, 3, 5, 5, 7, 7, 2, 9}
// We sort by highest frequency to lowest frequency.
// If two elements have same frequency, we sort by increasing value.
```

More examples in test cases.

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` and deconstructor `foldl` for your `List` encoding  
~~~

Good luck!

Please also try [Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)
"""

def solve(arr):
    key = lambda x: (-arr.count(x), x)
    return sorted(arr, key=key)
