"""Kata - Only Duplicates

completed at: 2024-08-12 16:11:26
by: Jakub Červinka

Given a string, remove any characters that are unique from the string.

Example: 

input: "abccdefee"

output: "cceee"

"""

from collections import Counter

def only_duplicates(st):
    c = Counter(st)
    return ''.join(l for l in st if c[l] > 1)
        
