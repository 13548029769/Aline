from random import randint

class Die():
    """class representative a dice"""
    def __init__(self,num_sides = 6):
        # dice has 6 sides by default
        self.num_sides = num_sides

    def roll(self):
        """return a number between 1 and num_sides"""
        return randint(1,self.num_sides)
