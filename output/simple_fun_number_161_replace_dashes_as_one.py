"""Kata - Simple Fun #161: Replace Dashes As One

completed at: 2024-07-31 11:28:12
by: Jakub Červinka

# Task
 If string has more than one neighboring dashes(e.g. --) replace they with one dash(-). 
 
 Dashes are considered neighbors even if there is some whitespace **between** them.

# Example

 For `str = "we-are- - - code----warriors.-"`
 
 The result should be `"we-are- code-warriors.-"`
 
# Input/Output


 - `[input]` string `str`
 
 
 - `[output]` a string
"""

import re

def replace_dashes_as_one(st):
    pattern = re.compile(r'-( *-)+')
    return pattern.sub('-', st)
