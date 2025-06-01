Question 7_______
Make a class Die with one attribute
called sides, which has a defaultvalue of 6. Write a method 
called roll_die() that prints a
random numberbetween 1 and the number of sides 
the die has. Make a 6-sided die and 
roll it10 times.


Solution ____________
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)
die_6 = Die()
print("Rolling 6-sided die 10 times:")
for _ in range(10):
    print(die_6.roll_die(), end=' ')
print()
die_10 = Die(10)
print("Rolling 10-sided die 10 times:")
for _ in range(10):
    print(die_10.roll_die(), end=' ')
print()
die_20 = Die(20)
print("Rolling 20-sided die 10 times:")
for _ in range(10):
    print(die_20.roll_die(), end=' ')
print()
