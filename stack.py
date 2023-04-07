# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:11:30 2023

@author: Robbins
"""

class Stack:
    def __init__(self):
        self._data = []
        
    def push(self, item):
        """ Add an item to the end of the list """
        self._data.append(item)
        
        # This also works, we just don't need both.
        # self._data += [item]
        
    def pop(self):
        """ Removes the last item from the Stack """
        # Grab the last item
        last_item = self._data[-1]
        
        # Remove the item from the _data list 
        self._data = self._data[:-1]
        
        # Return the saved item we grabbed
        return last_item
    
    def peek(self):
        """ Shows the last item in the Stack WITHOUT removing """
        return self._data[-1]
    
    def is_empty(self):
        return self._data == []
    
        # This is also valid, we just don't need both
        # return len(self._data) == 0

    def size(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)
        

def main():
    stack_1 = Stack()
    
    print(stack_1.is_empty()) # Expect True
    
    stack_1.push("Melissa")
    stack_1.push("Zelda")
    stack_1.push("Midna")
    stack_1.push("Impa")
    
    print(stack_1)
    
    popped = stack_1.pop()
    
    print(popped)
    print(stack_1)
    
    print(stack_1.peek())
    print(stack_1)
    
    print(stack_1.is_empty()) # Expect False
    print(stack_1.size())

    # stack_2 = Stack()
    
main()











