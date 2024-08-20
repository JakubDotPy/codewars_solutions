"""Kata - X marks the spot!

completed at: 2024-08-19 09:33:39
by: Jakub Červinka

Write a function ```x(n)``` that takes in a number ```n``` and returns an ```nxn``` array with an ```X``` in the middle. The ```X``` will be represented by ```1's``` and the rest will be ```0's```. <br/>
E.g.<br/>
```javascript
x(5) === [[1, 0, 0, 0, 1],
          [0, 1, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 0, 1, 0],
          [1, 0, 0, 0, 1]];
          
x(6) === [[1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 1]];
```
```python
x(5) ==  [[1, 0, 0, 0, 1],
          [0, 1, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 0, 1, 0],
          [1, 0, 0, 0, 1]];
          
x(6) ==  [[1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 1]];
```
```ruby
x(5) ==  [[1, 0, 0, 0, 1],
          [0, 1, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 0, 1, 0],
          [1, 0, 0, 0, 1]];
          
x(6) ==  [[1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 1]];
```
"""

def x(n):
    
    if n == 1: return [[1]]
    if n == 2: return [[1, 1], [1, 1]]
    
    res = [0] * n
    h = n // 2
    for i in range(h):
        l = [0] * i + [1] + [0] * (n - (2 * (i + 1))) + [1] + [0] * i
        res[i] = res[-i - 1] = l
    
    if n % 2 != 0:
        res[h] = [0] * h + [1] + [0] * h
    return res        