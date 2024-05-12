"""Kata - Who likes it?

completed at: 2019-03-05 12:38:33
by: Jakub Červinka

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

```
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```


```if:c
* return must be an allocated string
* do not mutate input
```

Note: For 4 or more names, the number in `"and 2 others"` simply increases.

"""

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return '{} likes this'.format(names[0])
    elif len(names) == 2:
        return '{} and {} like this'.format(*names)
    elif len(names) == 3:
        return '{}, {} and {} like this'.format(*names)
    else:
        return '{}, {} and {num} others like this'.format(*names[:2], num=len(names)-2)
