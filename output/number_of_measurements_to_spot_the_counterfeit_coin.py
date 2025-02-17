"""Kata - Number of measurements to spot the counterfeit coin

completed at: 2024-08-12 19:59:25
by: Jakub Červinka

<a style="float:right; margin:5px" href="https://www.youtube.com/watch?v=66tQR7koR_Q"><img alt="coins balance scale problem" src="https://activerain-store.s3.amazonaws.com/image_store/uploads/agents/kcrowson/files/Scale%20and%20Gold%20Coins.jpg"></a>I found this interesting interview question just today:

> *8 coins are given where all the coins have equal weight, except one. The odd one weights less than the others, not being of pure gold. In the worst case, how many iterations are actually needed to find the odd one out on a two plates scale*.

I am asking you then to tell me what is the *minimum* amount of weighings it will take to measure `n` coins in every possible occurrence (including worst case scenario, ie: without relying on luck at all).

`n` is guaranteed to be a positive integer.

***Tip:*** being able to think *recursively* might help here :p

***Note:*** albeit this is more clearly a logical than a coding problem, do not underestimate (or under-rank) the kata for requiring not necessarily wizard-class coding skills: a good coder is a master of pattern recognition and subsequent optimization ;)
"""

from math import log
from math import ceil

def how_many_measurements(n):
    return ceil(log(n, 3))
