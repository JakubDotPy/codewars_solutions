"""Kata - Controlled Detonation Safety

completed at: 2024-07-21 20:06:14
by: Jakub Červinka

# Context

The Explosive Ordinance Disposal Unit of your country has found a small mine field near your town, and is planning to perform a **controlled detonation** of all of the mines. They have tasked you to write an algorithm that helps them find **all safe spots in the area**, as they want to build a temporal base in the area where all workers can rest safely.

All mines they found are of a special kind, as they only release explosive charge in **four straight lines**, each pointing at a different cardinal point **(north, south, east and west)**. However, the charge stops spreading when it crosses a tree in its path because the charge is not strong enough to burn them.

In the following diagram, ```M``` represents a mine, ```C``` represents the explosive charge released after its detonation, and ```T``` are the trees in the area:

```
. . . . . . .    . . . . . . .
. . . T . . .    . . . T . . .
. . . . . . .    . . . C . . .
. . T M . . . => . . T M C C C
. . . . . . .    . . . C . . .
. . . . . . .    . . . C . . .
. . . T . . .    . . . T . . .
```

# Task

Write an algorithm that, given a mine field represented as an **array of arrays** of size ```M * N```, returns an **array of all safe positions** where workers can build their temporal base. As in the previous model, ```'M'``` represents mines, ```'T'``` represents trees, and ```'.'``` represents empty spaces where explosive charge can spread. The positions in the array **should be in "reading order"** (from left to right, and from up to down).

For example:

```
[
  ['.', '.', '.', '.', 'M'],                      . . . . M                           C C C C M
  ['.', 'M', '.', 'T', '.'],                      . M . T .                           C M C T C
  ['.', '.', 'T', '.', '.'],   ==[represents]=>   . . T . .   ==[after explosion]=>   . C T . C
  ['.', '.', 'M', '.', 'T'],                      . . M . T                           C C M C T
  ['.', '.', '.', '.', '.']                       . . . . .                           . C C . .
]
```
This should return one of the two following arrays, depending on the language. Check sample test cases for more information. Also, **trees don't count as safe positions**.

- ```[(2,0), (2,3), (4,0), (4,3), (4,4)] //For Python```
- ```[[2,0], [2,3], [4,0], [4,3], [4,4]] //For JS and other languages```

Return an empty array if there are no safe positions.

# Note

Mines will not stop explosive charge from spreading as trees do, and explosive charge won't erase mines it finds in its path. **Make sure you never override any mines in the field.**
"""

from operator import itemgetter

class MineField:
    
    directions = (
        (0, -1),  # up
        (1, 0),   # right
        (0, 1),   # down
        (-1, 0),  # left
    )
    
    def __init__(self):
        self.grid = dict()
        self.flame = set()
        self.mines = set()
        self.trees = set()
    
    def load_grid(self, mine_field):
        for y, row in enumerate(mine_field):
            for x, char in enumerate(row):
                self.grid[(x, y)] = char
                if char == 'M': self.mines.add((x, y))
                if char == 'T': self.trees.add((x, y))
    
    def explode(self, mine):
        for dx, dy in self.directions:
            x, y = mine
            while True:
                x, y = x + dx, y + dy
                if (x, y) in self.trees or (x, y) not in self.grid:
                    break
                self.flame.add((x, y))
    
    @property
    def safe_positions(self):
        return [
            (y, x)
            for x, y in sorted(
            set(self.grid.keys()) - self.mines - self.trees - self.flame,
            key=itemgetter(1, 0)
            )
        ]
                
    
def safe_mine_field(mine_field):
    mf = MineField()
    mf.load_grid(mine_field)
    for mine in mf.mines:
        mf.explode(mine)
    return mf.safe_positions
        
