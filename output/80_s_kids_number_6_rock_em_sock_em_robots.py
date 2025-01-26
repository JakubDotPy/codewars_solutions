"""Kata - 80's Kids #6: Rock 'Em, Sock 'Em Robots

completed at: 2025-01-25 20:34:00
by: Jakub Červinka

You and your friends have been battling it out with your Rock 'Em, Sock 'Em robots, but things have gotten a little boring. You've each decided to add some amazing new features to your robot and automate them to battle to the death.

Each robot will be represented by an object. You will be given two robot objects, and an object of battle tactics and how much damage they produce. Each robot will have a name, hit points, speed, and then a list of battle tactics they are to perform in order. Whichever robot has the best speed, will attack first with one battle tactic. 

Your job is to decide who wins.

Example:
```javascript
 robot1 = {
  "name": "Rocky",
  "health": 100,
  "speed": 20,
  "tactics": ["punch", "punch", "laser", "missile"]
 }
 robot2 = {
   "name": "Missile Bob",
   "health": 100,
   "speed": 21,
   "tactics": ["missile", "missile", "missile", "missile"]
 }
 tactics = {
   "punch": 20,
   "laser": 30,
   "missile": 35
 }
 
 fight(robot1, robot2, tactics) -> "Missile Bob has won the fight."
```
```coffeescript
robot1 =
  name: "Rocky"
  health: 100
  speed: 20
  tactics: [
    "punch", "punch", "laser", "missile"
  ]
robot2 =
  name: "Missile Bob"
  health: 100
  speed: 21
  tactics: [
    "missile", "missile", "missile", "missile"
  ]
tactics =
  punch: 20
  laser: 30
  missile: 35
 
fight(robot1, robot2, tactics) # "Missile Bob has won the fight."
```
```ruby
robot1 = {
  "name" => "Rocky",
  "health" => 100,
  "speed" => 20,
  "tactics" => ["punch", "punch", "laser", "missile"]
 }
 robot2 = {
   "name" => "Missile Bob",
   "health" => 100,
   "speed" => 21,
   "tactics" => ["missile", "missile", "missile", "missile"]
 }
 tactics = {
   "punch" => 20,
   "laser" => 30,
   "missile" => 35
 }
 
 fight(robot1, robot2, tactics) # "Missile Bob has won the fight."
```
```java
  robot1.getName() => "Rocky"
  robot1.getHealth() => 100
  robot1.getSpeed() => 20
  robot1.getTactics() => ["punch", "punch", "laser", "missile"]
    
  robot2.getName() => "Missile Bob"
  robot2.getHealth() => 100
  robot2.getSpeed() => 21
  robot2.getTactics() => ["missile", "missile", "missile", "missile"]
 
  tactics = {
    "punch" => 20,
    "laser" => 30,
    "missile" => 35
  }
 
 fight(Robot robot1, Robot robot2, Map<String, Integer> tactics) -> "Missile Bob has won the fight."
```
```python
 robot_1 = {
  "name": "Rocky",
  "health": 100,
  "speed": 20,
  "tactics": ["punch", "punch", "laser", "missile"]
 }
 robot_2 = {
   "name": "Missile Bob",
   "health": 100,
   "speed": 21,
   "tactics": ["missile", "missile", "missile", "missile"]
 }
 tactics = {
   "punch": 20,
   "laser": 30,
   "missile": 35
 }
 
 fight(robot_1, robot_2, tactics) -> "Missile Bob has won the fight."
```

robot2 uses the first tactic, "missile" because he has the most speed. This reduces robot1's health by 35. Now robot1 uses a punch, and so on. 

**Rules**

- A robot with the most speed attacks first. If they are tied, the first robot passed in attacks first.
- Robots alternate turns attacking. Tactics are used in order.
- A fight is over when a robot has 0 or less health or both robots have run out of tactics.
- A robot who has no tactics left does no more damage, but the other robot may use the rest of his tactics.
- If both robots run out of tactics, whoever has the most health wins. If one robot has 0 health, the other wins. Return the message "{Name} has won the fight."
- If both robots run out of tactics and are tied for health, the fight is a draw. Return "The fight was a draw."

**To Java warriors**

`Robot` class is immutable.

<div style="width: 320px; text-align: center; color: white; border: white 1px solid;">
Check out my other 80's Kids Katas:
</div>
<div>
<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-1-how-many-licks-does-it-take'><span style='color:#00C5CD'>80's Kids #1:</span> How Many Licks Does It Take</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-2-help-alf-find-his-spaceship'><span style='color:#00C5CD'>80's Kids #2:</span> Help Alf Find His Spaceship</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-3-punky-brewsters-socks'><span style='color:#00C5CD'>80's Kids #3:</span> Punky Brewster's Socks</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-4-legends-of-the-hidden-temple'><span style='color:#00C5CD'>80's Kids #4:</span> Legends of the Hidden Temple</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-5-you-cant-do-that-on-television'><span style='color:#00C5CD'>80's Kids #5:</span> You Can't Do That on Television</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-6-rock-em-sock-em-robots'><span style='color:#00C5CD'>80's Kids #6:</span> Rock 'Em, Sock 'Em Robots</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-7-shes-a-small-wonder'><span style='color:#00C5CD'>80's Kids #7:</span> She's a Small Wonder</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-8-the-secret-world-of-alex-mack'><span style='color:#00C5CD'>80's Kids #8:</span> The Secret World of Alex Mack</a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-9-down-in-fraggle-rock'><span style='color:#00C5CD'>80's Kids #9:</span> Down in Fraggle Rock </a><br />

<a style='text-decoration:none' href='http://www.codewars.com/kata/80-s-kids-number-10-captain-planet'><span style='color:#00C5CD'>80's Kids #10:</span> Captain Planet </a><br />


</div>

"""

from collections import deque
from itertools import cycle
from itertools import pairwise
from dataclasses import dataclass


class OutOfMoves(Exception):
    """Robot has no moves left."""


@dataclass
class Robot:
    name: str
    health: int
    speed: int
    tactics: deque[str]
    
    @classmethod
    def from_dict(cls, dct):
        return cls(
            dct["name"],
            dct["health"],
            dct["speed"],
            deque(dct["tactics"])
        )
    
    def attack(self, other, tactics):
        power = tactics[self.tactics.popleft()]
        other.health -= power
        
    @property
    def dead(self):
        return self.health <= 0
    
    @property
    def win_msg(self):
        return f'{self.name} has won the fight.'

    
def fight(robot_1, robot_2, tactics):
    
    robot_1 = Robot.from_dict(robot_1)
    robot_2 = Robot.from_dict(robot_2)
    
    robots = pairwise(cycle(sorted([robot_1, robot_2], key=lambda r: r.speed, reverse=True)))
    
    for r1, r2 in robots:
        if not (r1.tactics or r2.tactics):
            break
        
        if r1.tactics:
            r1.attack(r2, tactics)
        if r2.dead:
            return r1.win_msg
    
    if r1.health == r2.health:
        return 'The fight was a draw.'
    
    return [r1.win_msg, r2.win_msg][r1.health < r2.health]
        
