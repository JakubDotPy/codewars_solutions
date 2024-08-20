"""Kata - Reorder Array 2

completed at: 2024-08-12 18:26:17
by: Jakub Červinka

This kata focuses on the Numpy python package and you can read up on the Numpy array manipulation functions here: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html

You will get two integers `N` and `M`. You must return an array with two sub-arrays with numbers in ranges `[0, N / 2)` and `[N / 2, N)` respectively, each of them being rotated `M` times.

```
reorder(10, 1)   =>  [[4, 0, 1, 2, 3], [9, 5, 6, 7, 8]]
reorder(10, 3)   =>  [[2, 3, 4, 0, 1], [7, 8, 9, 5, 6]]
reorder(10, 97)  =>  [[3, 4, 0, 1, 2], [8, 9, 5, 6, 7]]
```
"""

import numpy as np

def reorder(n, r):
    half = n // 2
    arrays = [
        np.roll(np.arange(0, half), r).tolist(),
        np.roll(np.arange(half, n), r).tolist(),
    ]
    return arrays