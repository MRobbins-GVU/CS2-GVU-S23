from random import randint

class Die:
    """ A single n-sided die. """
    
    # Initilization function, run when a Die is created
    def __init__(self, num_sides):
        self.num_sides = num_sides
        # TODO: Update this line to roll with the correct number of sides.
        self.value = randint(1, 6)
        
    # Called using .roll() to generate a new random number
    def roll(self):
        # TODO: Update this line to roll with the correct number of sides.
        self.value = randint(1, 6)
        
    # Used to make print(Die) pretty
    def __str__(self):
        return str(self.value)
    
def main():
    #TODO: Using input, ask the user for the number of sides for each of these dice.
    #HINT: I recommend making the changes to main last.
    die1 = Die(10) # 10 sided die
    die2 = Die(20) # 20 sided die
    
    #TODO: Ask the user how many times to roll the dice
    for i in range(10):
        die1.roll()
        die2.roll()
        print(die1, die2)
    
main()
