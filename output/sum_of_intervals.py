"""Kata - Sum of Intervals

completed at: 2024-09-10 10:32:42
by: Jakub Červinka

Write a function called `sumIntervals`/`sum_intervals` that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

### Intervals

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: `[1, 5]` is an interval from `1` to `5`. The length of this interval is `4`.

### Overlapping Intervals

List containing overlapping intervals:

```c -- actual language id doesn't matter -- just want syntax highlighting
[
   [1, 4],
   [7, 10],
   [3, 5]
]
```

The sum of the lengths of these intervals is `7`. Since `[1, 4]` and `[3, 5]` overlap, we can treat the interval as `[1, 5]`, which has a length of `4`.

### Examples:

```c -- idem
sumIntervals( [
   [1, 2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030
```

### Tests with large intervals

Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range `[-1000000000, 1000000000]`.

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `ScottBinary` ( subsets are actually in range `[0, 2000]` )  
export constructor `Pair` for your `Pair` encoding  
export constructors `nil, cons` for your `List` encoding  
~~~

"""

def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    first = intervals[0]
    if len(intervals) == 1:
        return first[1] - first[0]

    merged_intervals = [list(first), ]

    for i_start, i_end in intervals[1:]:
        for i, (ci_start, ci_end) in enumerate(merged_intervals):
            starts_in = ci_start <= i_start <= ci_end
            ends_in = ci_start <= i_end <= ci_end
            if starts_in or ends_in:
                ci_start = min(ci_start, i_start)
                ci_end = max(ci_end, i_end)
                merged_intervals[i] = [ci_start, ci_end]
                break
        else:
            merged_intervals.append([i_start, i_end])

    total = sum(
        b - a
        for a, b in merged_intervals
    )
    return total
