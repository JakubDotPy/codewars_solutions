"""Kata - Message Validator

completed at: 2024-09-06 18:51:26
by: Jakub Červinka

In this kata, you have an input string and you should check whether it is a valid message. To decide that, you need to split the string by the numbers, and then compare the numbers with the number of characters in the following substring.

For example `"3hey5hello2hi"` should be split into `3, hey, 5, hello, 2, hi` and the function should return `true`, because `"hey"` is 3 characters, `"hello"` is 5, and `"hi"` is 2; as the numbers and the character counts match, the result is `true`.
      
      
**Notes:**
* Messages are composed of only letters and digits
* Numbers may have multiple digits: e.g. `"4code13hellocodewars"` is a valid message
* Every number must match the number of character in the following substring, otherwise the message is invalid: e.g. `"hello5"` and `"2hi2"` are invalid
* If the message is an empty string, you should return `true`

"""

import re
from itertools import tee
from itertools import islice
from itertools import zip_longest

def is_a_valid_message(message):
    parts = re.split(r'(\d+)', message)
    parts = filter(None, parts)  # remove empty strings
    
    # prepare iterators
    first_it, second_it = tee(parts, 2)
    
    nums = islice(first_it, 0, None, 2)
    nums = map(int, nums)
    texts = islice(second_it, 1, None, 2)
    
    try:
        for num, text in zip_longest(nums, texts):
            assert len(text) == num
    except (AssertionError, ValueError, TypeError):
        return False
    
    # all passed
    return True
