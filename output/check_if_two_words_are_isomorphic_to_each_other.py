"""Kata - Check if two words are isomorphic to each other

completed at: 2024-07-16 19:12:08
by: Jakub Červinka

Two strings ```a``` and b are called isomorphic if there is a one to one mapping possible for every character of ```a``` to every character of ```b```. And all occurrences of every character in ```a``` map to same character in ```b```.

## Task

In this kata you will create a function that return ```True``` if two given strings are isomorphic to each other, and ```False``` otherwise. Remember that order is important.

Your solution must be able to handle words with more than 10 characters.

## Example
True:
```
CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS
```

False:
```
AB CC
XXY XYY
ABAB CD
```
"""

def isomorph(a, b):
    try:
        forward = str.maketrans(a, b)
        back = str.maketrans(b, a)
        return (a.translate(forward) == b) and (b.translate(back) == a)
    except ValueError:
        return False
            
