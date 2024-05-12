"""Kata - ROT13

completed at: 2023-06-15 07:48:04
by: Jakub Červinka

How can you tell an extrovert from an introvert at NSA?  
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?  
According to Wikipedia, [ROT13](http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

```
"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
```

"""

import codecs

def rot13(message):
    return codecs.encode(message, 'rot13')
