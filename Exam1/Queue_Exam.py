# -*- coding: utf-8 -*-
"""
Created on Thu Apr  13 18:23:32 2023

@author: Robbins
"""

class Queue:
    
    def __init__(self):
        self._items = []
        
    def insert(self, item):
        """ Adds to the front of the list """
        self._items = [item] + self._items
        
    def remove(self):
        """ Remove the last item of the list """
        # Grab the last item
        last_item = self._items[-1]
        
        # Remove the last item from the list
        self._items = self._items[:-1]
        
        # Return the last_item we grabbed
        return last_item
      
    def remove_item(self, item):
        """ Remove item from the queue, if it is in the queue """
        # TODO: check if item is in the queue. 
            # TODO: remove the item from the queue somehow
            # TODO: return item after removing
    
    def peek(self):
        """ Return the item at the front of the Queue (the end of the list) """
        return self._items[-1]
        
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)
    
def main():
    queue1 = Queue()
    print(queue1.is_empty()) # Expecting True
    
    queue1.insert("Dinraal")
    queue1.insert("Ganon")
    queue1.insert("Igneel")
    queue1.insert("Impa")
    queue1.insert("Midna")
    queue1.insert("Zelda")
    
    print(queue1) # Expecting ["Zelda", "Midna", "Impa", "Igneel", "Ganon", "Dinraal"]
    
    print(queue1.remove_item("Igneel")) # Expecting Igneel
    print(queue1) # Expecting ["Zelda", "Midna", "Impa", "Ganon", "Dinraal"] 
    
    
main()





