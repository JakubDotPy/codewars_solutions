"""Kata - Odder Than the Rest

completed at: 2019-09-24 05:55:31
by: Jakub Červinka

```if-not:swift
Create a method that takes an array/list as an input, and outputs the index at which the sole odd number is located.

This method should work with arrays with negative numbers. If there are no odd numbers in the array, then the method should output `-1`.
```
```if:swift
reate a function `oddOne` that takes an `[Int]` as input and outputs the index at which the sole odd number is located.

This method should work with arrays with negative numbers. If there are no odd numbers in the array, then the method should output `nil`.
```
Examples:
```ruby
oddOne([2,4,6,7,10]) # => 3
oddOne([2,16,98,10,13,78]) # => 4
oddOne([4,-8,98,-12,-7,90,100]) # => 4
oddOne([2,4,6,8]) # => -1
```
```javascript
oddOne([2,4,6,7,10]) // => 3
oddOne([2,16,98,10,13,78]) // => 4
oddOne([4,-8,98,-12,-7,90,100]) // => 4
oddOne([2,4,6,8]) // => -1
```
```python
odd_one([2,4,6,7,10]) # => 3
odd_one([2,16,98,10,13,78]) # => 4
odd_one([4,-8,98,-12,-7,90,100]) # => 4
odd_one([2,4,6,8]) # => -1
```
```haskell
oddOne [2,4,6,7,10]            -- ->  3
oddOne [2,16,98,10,13,78]      -- ->  4
oddOne [4,-8,98,-12,-7,90,100] -- ->  4
oddOne [2,4,6,8]               -- -> -1
```
```csharp
Kata.OddOne(new List<int> {2,4,6,7,10}) => 3
Kata.OddOne(new List<int> {2,16,98,10,13,78}) => 4
Kata.OddOne(new List<int> {4,-8,98,-12,-7,90,100}) => 4
Kata.OddOne(new List<int> {2,4,6,8}) => -1
```
```swift
oddOne([2,4,6,7,10]) // => 3
oddOne([2,16,98,10,13,78]) // => 4
oddOne([4,-8,98,-12,-7,90,100]) // => 4
oddOne([2,4,6,8]) // => nil
```
```c
odd_one({2, 4, 6, 7, 10}, 5);              // ==  3
odd_one({2, 16, 98, 10, 13, 78}, 6);       // ==  4
odd_one({4, -8, 98, -12, -7, 90, 100}, 7); // ==  4
odd_one({2, 4, 6, 8}, 4);                  // == -1
```
"""

def odd_one(arr):
    for i, v in enumerate(arr):
        if v % 2 == 1:
            return i
    return -1
