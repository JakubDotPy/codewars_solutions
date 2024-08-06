"""Kata - Inserting multiple strings into another string

completed at: 2024-08-05 11:51:17
by: Jakub Červinka

Dear Coder,

We at [SomeLargeCompany] have decided to expand on the functionality of our online text editor.

We have written a new function that accepts a phrase, a word and an array of indexes.
We want this function to return the phrase, with the word inserted at each of the indexes given by the array.

However, our current function only gets the first insertion right, but all of the following ones are out of place!

Please fix this for us, and you will be showered with money.

Yours Sincerely,
[SomeLargeCompany]

Note :

- the indicies are always in range and passed as a sorted array
- note if the index array is empty, just return the initial phrase
"""

def insert_at_indexes(phrase, word, indexes): 
    for i in reversed(indexes): 
        phrase = phrase[:i] + word + phrase[i:]
    return phrase
