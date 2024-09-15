"""Kata - Invert values

completed at: 2024-09-14 15:23:07
by: Jakub Červinka

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
```

```if:javascript,python,ruby,php,elixir,dart,go,lua
You can assume that all values are integers. Do not mutate the input array.
```

```if:c,riscv
### Notes:
- All values are greater than `INT_MIN`
- The input should be modified, not returned.
```

~~~if:riscv
RISC-V: The function signature is:

```c
void invert(int *arr, size_t size);
```

The input array is `arr` which contains `size` elements. Mutate the array in-place according to the above specification. You do not need to return anything.
~~~

"""

def invert(lst):
    vysledek = []
    for cislo in lst:
        vysledek.append(-cislo)
    return vysledek
