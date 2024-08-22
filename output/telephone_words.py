"""Kata - telephone words

completed at: 2024-08-21 18:44:14
by: Jakub Červinka

Businesses use keypad letters in creative ways to spell out a phone number and make it more memorable. 
Example:
 http://en.wikipedia.org/wiki/File:Telephone-keypad2.svg

Create a mapping for your dialer as given in the above link.
Constraints: 
1. letters are all uppercase
2. digits 0, 1 are mapped to 0, 1 respectively

Write a function that takes four digits of a phone number, and returns a list of all of the words that can be written with that number. (You should return all permutations, not only English words.)

"""

from itertools import product

def telephone_words(digit_string):
    mapping = {
        '0': '0',
        '1': '1',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    options = (
        mapping[letter]
        for letter in digit_string
    )
    return list(''.join(tup) for tup in product(*options))
    
