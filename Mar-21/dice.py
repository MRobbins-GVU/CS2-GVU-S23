#rolldice.py

from random import randint

class Die:
    """ A single 6-sided die. """
    
    def __init__(self):
        self.value = randint(1, 6)
        
    def roll(self):
        self.value = randint(1, 6)
        
    def __str__(self):
        return str(self.value)
    
def main():
    die1 = Die() 
    die2 = Die()
    
    for i in range(10):
        die1.roll()
        die2.roll()
        print(die1, die2)
    
main()
