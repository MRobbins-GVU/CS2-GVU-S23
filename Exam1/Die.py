from random import randint

class Die:
    """ A single n-sided die. """
    
    # Initilization function, run when a Die is created
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.value = randint(1, num_sides)
        
    # Called using .roll() to generate a new random number
    def roll(self):
        self.value = randint(1, self.num_sides)
        
    def roll_with_result(self):
        # TODO: roll the die
        
        # TODO: Fill in the if/elif/else block using the chart of values from rolling
        if self.value == 1:
            print("")
        
    # Used to make print(Die) pretty
    def __str__(self):
        return str(self.value)
    
def main():
    die1_value = int(input("Enter the number of sides for the die: "))

    die1 = Die(die1_value) 
    
    die1.roll_with_result()

    
main()
