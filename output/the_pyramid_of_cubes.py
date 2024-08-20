"""Kata - The Pyramid of Cubes

completed at: 2024-08-19 08:23:14
by: Jakub Červinka

The workers of CodeLand intend to build a brand new building in the town centre after the end of the 3rd Code Wars.

They intend to build a triangle-based pyramid (tetrahedron) out of cubes.

They require a program that will find the tallest potential height of the pyramid, given a certain number of cubes.

Your function needs to return the pyramid with largest number of full layers possible with the input.

The input will be an integer of how many cubes are available, and your output should return the height of the tallest pyramid buildable with that number of cubes.

The schematic below shows a **cross-section** of each layer of the pyramid, top down:


Layer 1 -
  
              x


Layer 2 -

              x
            x   x
            
Layer 3 - 

              x
            x   x
          x   x   x
"""

from itertools import count

def gen_pyramid():
    """Tn = (n * (n + 1))/2"""
    total = 0
    for n in count():
        next_layer = (n * (n + 1))/2
        total += next_layer
        yield n, total
        

def find_height(cubes):
    for height, count in gen_pyramid():
        if count == cubes:
            return height
        elif count > cubes:
            return height - 1
