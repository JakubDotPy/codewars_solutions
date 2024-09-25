"""Kata - Nesting Structure Comparison

completed at: 2024-09-24 14:35:36
by: Jakub Červinka

Complete the function/method (depending on the language) to return `true`/`True` when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

```javascript
 // should return true
[ 1, 1, 1 ].sameStructureAs( [ 2, 2, 2 ] );          
[ 1, [ 1, 1 ] ].sameStructureAs( [ 2, [ 2, 2 ] ] );  

 // should return false 
[ 1, [ 1, 1 ] ].sameStructureAs( [ [ 2, 2 ], 2 ] );  
[ 1, [ 1, 1 ] ].sameStructureAs( [ [ 2 ], 2 ] );  

// should return true
[ [ [ ], [ ] ] ].sameStructureAs( [ [ [ ], [ ] ] ] ); 

// should return false
[ [ [ ], [ ] ] ].sameStructureAs( [ [ 1, 1 ] ] );     
```
```php
same_structure_as([1, 1, 1], [2, 2, 2]); // => true
same_structure_as([1, [1, 1]], [2, [2, 2]]); // => true
same_structure_as([1, [1, 1]], [[2, 2], 2]); // => false
same_structure_as([1, [1, 1]], [[2], 2]); // => false
same_structure_as([[[], []]], [[[], []]]); // => true
same_structure_as([[[], []]], [[1, 1]]); // => false
```
```ruby
# should return true
[ 1, 1, 1 ].same_structure_as( [ 2, 2, 2 ] )
[ 1, [ 1, 1 ] ].same_structure_as( [ 2, [ 2, 2 ] ] )

# should return false 
[ 1, [ 1, 1 ] ].same_structure_as( [ [ 2, 2 ], 2 ] )
[ 1, [ 1, 1 ] ].same_structure_as( [ [ 2 ], 2 ] )

# should return true
[ [ [ ], [ ] ] ].same_structure_as( [ [ [ ], [ ] ] ] ); 

# should return false
[ [ [ ], [ ] ] ].same_structure_as( [ [ 1, 1 ] ] )   
```
```python
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
```

~~~if:javascript
For your convenience, there is already a function 'isArray(o)' declared and defined that returns true if its argument is an array, false otherwise.
~~~

~~~if:php
You may assume that all arrays passed in will be non-associative.
~~~
"""

import ast

class StructureVisitor(ast.NodeVisitor):
    def __init__(self):
        self.structure = []
    
    def visit_List(self, node):
        """special method called when visiting list"""
        self.structure.append('list')
        for elem in node.elts:
            self.visit(elem)
        self.structure.append('end_list')
        
    def visit_Constant(self, node):
        self.structure.append('const')

def get_structure(expr):
    tree = ast.parse(str(expr), mode='eval')
    visitor = StructureVisitor()
    visitor.visit(tree)
    return visitor.structure
    
def same_structure_as(original, other):
    structure1 = get_structure(original)
    structure2 = get_structure(other)
    print(structure1, structure2)
    return structure1 == structure2

