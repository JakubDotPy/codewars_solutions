"""Kata - Splitting the Workload (part I)

completed at: 2024-09-10 09:50:23
by: Jakub Červinka

Imagine you have a number of jobs to execute. Your workers are not permanently connected to your network, so you have to distribute all your jobs in the beginning. Luckily, you know exactly how long each job is going to take. 

Let 
```
x = [2,3,4,6,8,2]
```
be the amount of time each of your jobs is going to take.

Your task is to write a function ```splitlist(x)```, that will return two lists ```a``` and ```b```, such that ```abs(sum(a)-sum(b))``` is minimised.

One possible solution to this example would be 
```
a=[2, 4, 6]
b=[3, 8, 2]
```
with  ```abs(sum(a)-sum(b)) == 1```.

The order of the elements is not tested, just make sure that you minimise ```abs(sum(a)-sum(b))``` and that ```sorted(a+b)==sorted(x)```.

You may assume that ```len(x)<=15``` and ```0<=x[i]<=100```.

When done, please continue with [part II](https://www.codewars.com/kata/586e6b54c66d18ff6c0015cd)!


"""

import itertools

def split_list(x):
    n = len(x)
    
    # edge case
    if n == 1:
        return x, []
    
    best_diff = float('inf')
    best_a, best_b = [], []

    for i in range(1, n // 2 + 1):  # only need to check half of the list length
        for subset in itertools.combinations(x, i):
            a = list(subset)
            
            b = x.copy()
            for elem in a:
                b.remove(elem)

            diff = abs(sum(a) - sum(b))

            if diff < best_diff:
                best_diff = diff
                best_a, best_b = a, b

            if best_diff == 0:
                return best_a, best_b
    print(best_a, best_b)
    return best_a, best_b

