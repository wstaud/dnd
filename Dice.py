"""Dice Class"""
import random

class Dice:
    def __init__(self, sides=20, rolls = 1):
        self.sides = int(sides)
        self.rolls = int(rolls)

    def roll(self):
        if self.rolls > 1:
            i = 0
            self.die_rolls = []
            while i < self.rolls:
                self.die_rolls.append(random.randint(1, self.sides))
                i += 1
            return self.die_rolls
        else:
            return random.randint(1, self.sides)








