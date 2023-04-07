# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:40:32 2023

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
    
    print(queue1)
    
    print(queue1.remove())
    
    print(queue1.is_empty()) # Expecting False
    
    print(queue1)
    
    print(queue1.peek())
    
    
main()






