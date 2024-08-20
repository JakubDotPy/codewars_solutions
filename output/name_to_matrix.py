"""Kata - Name to Matrix

completed at: 2024-08-19 08:48:28
by: Jakub Červinka

Given a name, turn that name into a perfect square matrix (nested array with the amount of arrays equivalent to the length of each array). 

You will need to add periods (`.`) to the end of the name if necessary, to turn it into a matrix. 

If the name has a length of 0, return `"name must be at least one letter"`

## Examples

```javascript
"Bill" ==> [ ["B", "i"],
             ["l", "l"] ]

"Frank" ==> [ ["F", "r", "a"],
              ["n", "k", "."],
              [".", ".", "."] ]
```

"""

import math
import numpy as np

def matrixfy(text):
    orig_len = len(text)
    
    if orig_len == 0:
        return "name must be at least one letter"
    
    side = math.ceil(orig_len ** 0.5)
    padding = (side * side) - orig_len
    to_reshape = text + ('.' * padding)
    
    arr = np.array(list(to_reshape)).reshape(side, side)
    return arr.tolist()
