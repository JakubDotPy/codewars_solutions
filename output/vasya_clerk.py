"""Kata - Vasya - Clerk

completed at: 2019-10-07 07:58:20
by: Jakub Červinka

Removed due to copyright infringement.

<!----

The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single `100`, `50` or `25` dollar bill. An "Avengers" ticket costs `25 dollars`.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line. 

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return `YES`, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return `NO`.


### Examples:

```csharp 
Line.Tickets(new int[] {25, 25, 50}) // => YES 
Line.Tickets(new int[] {25, 100}) // => NO. Vasya will not have enough money to give change to 100 dollars
Line.Tickets(new int[] {25, 25, 50, 50, 100}) // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```java
Line.Tickets(new int[] {25, 25, 50}) // => YES 
Line.Tickets(new int[] {25, 100}) // => NO. Vasya will not have enough money to give change to 100 dollars
Line.Tickets(new int[] {25, 25, 50, 50, 100}) // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```python
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```javascript
tickets([25, 25, 50]) // => YES 
tickets([25, 100]) // => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```haskell
tickets [25, 25, 50] -- -> YES 
tickets [25, 100] -- -> NO. Vasya will not have enough money to give change to 100 dollars
tickets [25, 25, 50, 50, 100] -- -> NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```cpp 
tickets({25, 25, 50}) // => YES 
tickets({25, 100}) // => NO. Vasya will not have enough money to give change to 100 dollars
tickets({25, 25, 50, 50, 100}) // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```go
Tickets([]int{25, 25, 50}) // => YES
Tickets([]int{25, 100}) // => NO. Vasya will not have enough money to give change to 100 dollars
Tickets([]int{25, 25, 50, 50, 100}) // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```fsharp
tickets [25; 25; 50] // => YES 
tickets [25; 100] // => NO. Vasya will not have enough money to give change to 100 dollars
tickets [25; 25; 50; 50; 100] // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```ruby
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
```c
tickets(3, {25, 25, 50}) // => true
tickets(2, {25, 100}) // => false. Vasya will not have enough money to give change to 100 dollars
tickets(5, {25, 25, 50, 50, 100}) // => false. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```

--->
"""

def tickets(people):
    from collections import Counter
    cash = Counter()
    ticket_price = 25
    noms = [100, 50, 25]
    for note in people:
        cash[note] += 1  # take the note
        to_return = note - ticket_price
        if to_return == 0: continue
        for nom in noms:  # try to give change back
            while cash.get(nom, False) and to_return - nom >= 0:
                cash[nom] -= 1
                to_return -= nom                
        if to_return != 0: return 'NO'
    return "YES"

