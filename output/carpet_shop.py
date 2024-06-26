"""Kata - Carpet shop

completed at: 2024-06-03 13:17:17
by: Jakub Červinka

A carpet shop sells carpets in different varieties. Each carpet can come in a different roll width and can have a different price per square meter. 

Write a function `cost_of_carpet` which calculates the cost (rounded to 2 decimal places) of carpeting a room, following these constraints:

* The carpeting has to be done in one unique piece. If not possible, retrun `"error"`.
* The shop sells any length of a roll of carpets, but always with a full width.
* The cost has to be minimal.
* The length of the room passed as argument can sometimes be shorter than its width (because we define these relatively to the position of the door in the room).
* A length or width equal to zero is considered invalid, return `"error"` if it occurs.

<hr>
<h1>INPUTS:

`room_width`, `room_length`, `roll_width`, `roll_cost` as floats.

<h1>OUTPUT:

`"error"` or the minimal cost of the room carpeting, rounded to two decimal places.
"""

def cost_of_carpet(room_length, room_width, roll_width, roll_cost):
    
    invalid_dimension = not (room_length or room_width)
    too_big_room = roll_width < min((room_length, room_width))
    
    if invalid_dimension or too_big_room:
        return 'error'
    
    
    if room_length < roll_width and room_width < roll_width:
        fn = min
    else:
        fn = max
        
    price = fn((room_length, room_width)) * roll_width * roll_cost

    return round(price, 2)

