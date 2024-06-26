"""Kata - Excel's COUNTIF, SUMIF and AVERAGEIF functions

completed at: 2024-06-07 19:33:33
by: Jakub Červinka

##The Brief
Microsoft Excel provides a number of useful functions for counting, summing, and averaging values if they meet a certain criteria. Your task is to write three functions that work similarly to Excel's COUNTIF, SUMIF and AVERAGEIF functions.

##Specifications
Each function will take the same two arguments:

* A list object containing `values` to be counted, summed, or averaged.
* A `criteria` in either an integer, float, or string
    * Integer or float indicates equality
    * Strings can indicate >, >=, <, <= or <> (use the Excel-style "Not equal to" operator) to a number (ex. ">=3"). In the `count_if` function, a string without an operater indicates equality to this string.
    
The tests will all include properly formatted inputs. The test cases all avoid rounding issues associated with floats.

##Examples
 ```python
count_if([1,3,5,7,9], 3)
1

count_if(["John","Steve","John"], "John")
2

sum_if([2,4,6,-1,3,1.5],">0")
16.5

average_if([99,95.5,0,83],"<>0")
92.5
```

##Excel Function Documentation:
* [COUNTIF](https://support.office.com/en-us/article/COUNTIF-function-e0de10c6-f885-4e71-abb4-1f464816df34)
* [SUMIF](https://support.office.com/en-us/article/SUMIF-function-169b8c99-c05c-4483-a712-1697a653039b)
* [AVERAGEIF](https://support.office.com/en-us/article/AVERAGEIF-function-faec8e2e-0dec-4308-af69-f5576d8ac642)
"""

from functools import partial
from operator import gt, ge, lt, le, ne, eq

def fn_from_criteria(criteria):
    if isinstance(criteria, (int, float)):
        fn, val = eq, criteria
        return partial(fn, val)
    
    # fns are inverted due to partial
    str_to_op = {
        '>=': le,
        '<=': ge,
        '<>': ne,
        '<' : gt,
        '>' : lt,
    }
    for op_str, op in str_to_op.items():
        if criteria.startswith(op_str):
            fn = op
            val = float(criteria.lstrip(op_str))
            print(fn, val)
            return partial(fn, val)
    
    fn, val = eq, criteria
    print(fn)
    return partial(fn, val)


def count_if(values,criteria):
    fn = fn_from_criteria(criteria)
    return sum(1 for v in values if fn(v))
    
def sum_if(values,criteria):
    fn = fn_from_criteria(criteria)
    return sum(v for v in values if fn(v))
    
def average_if(values,criteria):
    return sum_if(values,criteria) / count_if(values,criteria)
