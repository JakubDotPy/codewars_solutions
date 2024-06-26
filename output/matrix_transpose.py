"""Kata - Matrix Transpose

completed at: 2023-05-30 10:52:06
by: Jakub Červinka

Write a function that outputs the transpose of a matrix - a new matrix
where the columns and rows of the original are swapped.

For example, the transpose of:
  
    | 1 2 3 |
    | 4 5 6 |

is

    | 1 4 |
    | 2 5 |
    | 3 6 |

The input to your function will be an array of matrix rows. You can
assume that each row has the same length, and that the height and
width of the matrix are both positive.

~~~if:lambdacalc
#### Encodings

purity: `LetRec`  
numEncoding: `None`  
export constructors `nil, cons` and deconstructor `foldl` for your `List` encoding  
~~~

"""

def transpose(matrix):
    return list(map(list, zip(*matrix)))

