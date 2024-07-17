"""Kata - Which filetypes are you using the most?

completed at: 2024-07-16 19:37:03
by: Jakub Červinka

## Description

You've been working with a lot of different file types recently as your interests have broadened.

But what file types are you using the most? With this question in mind we look at the following problem.

Given a `List/Array` of Filenames (strings) `files` return a `List/Array of string(s)` containing the most common extension(s). If there is a tie, return a sorted list of all extensions.

### Important Info:

* Don't forget, you've been working with a lot of different file types, so expect some interesting extensions/file names/lengths in the random tests.
* Filenames and extensions will only contain letters (case sensitive), and numbers.
* If a file has multiple extensions (ie: `mysong.mp3.als`) only count the last extension (`.als` in this case)


## Examples

```
files = ['Lakey - Better days.mp3', 
         'Wheathan - Superlove.wav', 
         'groovy jam.als', 
         '#4 final mixdown.als', 
         'album cover.ps', 
         'good nights.mp3']
```

would return: `['.als', '.mp3']`, as both of the extensions appear two times in files.

```
files = ['Lakey - Better days.mp3', 
         'Fisher - Stop it.mp3', 
         'Fisher - Losing it.mp3', 
         '#4 final mixdown.als', 
         'album cover.ps', 
         'good nights.mp3']
```
would return `['.mp3']`, because it appears more times then any other extension, and no other extension has an equal amount of appearences.
"""

from collections import Counter
from pathlib import Path

def solve(files):
    paths = map(Path, files)
    counts = Counter(f.suffix for f in paths)
    m = max(counts.values(), default=0)
    return sorted(suffix for suffix, cnt in counts.items() if cnt == m)
