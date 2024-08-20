"""Kata - Check the status of the generator expression

completed at: 2024-08-19 09:55:02
by: Jakub Červinka

My third kata, write a function `check_generator` that examines the status of a Python generator expression `gen` and returns `'Created'`, `'Started'` or `'Finished'`. For example:

`gen = (i for i in range(1))` >>> returns `'Created'` (the generator has been initiated)

`gen = (i for i in range(1)); next(gen, None)` >>> returns `'Started'` (the generator has yielded a value)

`gen = (i for i in range(1)); next(gen, None); next(gen, None)` >>> returns `'Finished'` (the generator has been exhuasted)

For an introduction to Python generators, read: https://wiki.python.org/moin/Generators.

Please do vote and rank the kata, and provide any feedback.

Hint: you can solve this if you know the right module to use.
"""

import inspect

def check_generator(gen):
    state = inspect.getgeneratorstate(gen)
    translate = {
        'GEN_CREATED'  : 'Created',
        'GEN_SUSPENDED': 'Started',
        'GEN_CLOSED'   : 'Finished',
    }
    return translate[state] 
    

