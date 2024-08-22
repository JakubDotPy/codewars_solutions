"""Kata - Exercise in Summing

completed at: 2024-08-21 17:33:03
by: Jakub Červinka

Your task is to finish two functions, `minimumSum` and `maximumSum`, that take 2 parameters:

- `values`: an array of integers with an arbitrary length; may be positive and negative
- `n`: how many integers should be summed; always 0 or bigger

### Example:

```javascript
var values = [5, 4, 3, 2, 1];
minimumSum(values, 2); // should return 1+2 = 3
maximumSum(values, 3); // should return 3+4+5 = 12
```

```coffeescript
values = [5, 4, 3, 2, 1]
minimumSum values, 2 # should return 1+2 = 3
maximumSum values, 3 # should return 3+4+5 = 12
```

```python
values = [5, 4, 3, 2, 1];
minimum_sum(values, 2) #should return 1 + 2 = 3
maximum_sum(values, 3) #should return 3 + 4 + 5 = 12
```

```haskell
minimumSum [1..5] 2 `shouldBe` 1 + 2
minimumSum [1..5] 3 `shouldBe` 1 + 2 + 3
maximumSum [1..5] 2 `shouldBe`     4 + 5
maximumSum [1..5] 3 `shouldBe` 3 + 4 + 5
```

All values given to the functions will be integers. Also take care of the following special cases:

- if `values` is empty, both functions should return 0
- if `n` is 0, both functions should also return 0
- if `n` is larger than `values`'s length, use the length instead.
"""

def minimum_sum(values, n):
    return sum(sorted(values)[:n])

def maximum_sum(values, n):
    if n == 0: return 0
    return sum(sorted(values)[-n:])
