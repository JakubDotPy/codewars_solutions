"""Kata - Sort arrays - 3

completed at: 2024-11-03 09:37:13
by: Jakub Červinka

This time the input is a sequence of course-ids that are formatted in the following way:
```ruby
name-yymm
```
The return of the function shall first be sorted by <strong>yymm</strong>, then by the name (which varies in length).
"""

def sorting_fn(elem):
    name, yymm = elem.split('-')
    yy, mm = yymm[:2], yymm[2:]
    return yy, mm, name


def sort_me(courses):
    return sorted(courses, key=sorting_fn)
