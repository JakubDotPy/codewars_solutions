"""Kata - Let's Recycle!

completed at: 2023-05-04 07:17:44
by: Jakub Červinka

## Task

You will be given a list of objects. Each object has `type`, `material`, and possibly `secondMaterial`. The existing materials are: `paper`, `glass`, `organic`, and `plastic`.

Your job is to sort these objects across the 4 recycling bins according to their `material` (and `secondMaterial` if it's present), by listing the `type`'s of objects that should go into those bins.

### Notes

* The bins should come in the same order as the materials listed above
* All bins should be listed in the output, even if some of them are empty
* If an object is made of two materials, its `type` should be listed in both of the respective bins
* The order of the `type`'s in each bin should be the same as the order of their respective objects was in the input list

```if:python
* Contrary to the example below, the output in Python should be a tuple of 4 lists instead of a 2-dimensional list
```

### Example

```
input = [
  {"type": "rotten apples", "material": "organic"},
  {"type": "out of date yogurt", "material": "organic", "secondMaterial": "plastic"},
  {"type": "wine bottle", "material": "glass", "secondMaterial": "paper"},
  {"type": "amazon box", "material": "paper"},
  {"type": "beer bottle", "material": "glass", "secondMaterial": "paper"}
]

output = [
  ["wine bottle", "amazon box", "beer bottle"],
  ["wine bottle", "beer bottle"],
  ["rotten apples", "out of date yogurt"],
  ["out of date yogurt"]
]
```
"""

def recycle(a):
    bins = {
        'paper': [],
        'glass': [],
        'organic': [],
        'plastic': [],
    }
    
    for object in a:
        if material := object.get('material'):
            bins[material].append(object['type'])
    
        if second_material := object.get('secondMaterial'):
            bins[second_material].append(object['type'])
    
    return tuple(bins.values())
