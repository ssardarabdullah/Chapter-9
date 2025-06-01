import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# 6-sided die
die_6 = Die()
print("Rolling 6-sided die 10 times:")
for _ in range(10):
    print(die_6.roll_die(), end=' ')
print()

# 10-sided die
die_10 = Die(10)
print("Rolling 10-sided die 10 times:")
for _ in range(10):
    print(die_10.roll_die(), end=' ')
print()

# 20-sided die
die_20 = Die(20)
print("Rolling 20-sided die 10 times:")
for _ in range(10):
    print(die_20.roll_die(), end=' ')
print()