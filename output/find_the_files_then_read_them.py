"""Kata - Find the files then read them

completed at: 2024-07-16 19:30:01
by: Jakub Červinka

Find all files in the current directory where you run your code, then make a dictionary in the following manner. 


```
{ filename : first line of the file , ...}
```


"""

from pathlib import Path

def create_file_dict():
    result = dict()
    for item in Path.cwd().iterdir():
        if item.is_file():
            with item.open() as f:  
                result[item.name] = f.readline()
    return result
