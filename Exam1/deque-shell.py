
class Deque:
    def __init__(self):
        self.values = []
        
    def add_front(self, item):
        """ Adds to the front of the deque """
        # TODO
            
    def add_rear(self, item):
        """ Adds to the rear of the deque """
        # TODO
        
    def remove_front(self):
        """ Remove the item at the front of the deque and 
            return it """
        # Grab the item at the front of the deque    
        front_item = self.values[-1]
        
        # Remove the item from the front of the deque
        self.values = self.values[:-1] 
        
        # Return the item we grabbed
        return front_item
        
    def remove_rear(self):
        """ Remove the item at the rear of the deque and
            return it """ 
        # Grab the item at the rear of the deque
        rear_item = self.values[0]
        
        # Remove the item from the rear of the deque
        self.values = self.values[1:]  
        
        # Return the item we grabbed
        return rear_item
        
    def reverse(self):
        """ Reverses the order of the items in the deque, without changing the behavior """
        # TODO
        
    def is_empty(self):
        return len(self.values) == 0
    
    def size(self):
        return len(self.values) 
        
    def __str__(self):
        return str(self.values)
    
def main():
    deque1 = Deque()
    print(deque1.is_empty()) # should return True
    
    deque1.add_front('cat')
    deque1.add_rear('dog')
    deque1.add_rear('shark')
    deque1.add_front('lion')
    print(deque1) # expecting shark, dog, cat, lion
    
    print(deque1.size()) #should be 4
    
    deque1.reverse() # expecting lion, cat, dog, shark
    
    
main()
