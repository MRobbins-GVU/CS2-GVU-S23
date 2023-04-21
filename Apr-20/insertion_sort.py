# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:28:43 2023

@author: Robbins
"""

def insertion_sort(items):
    """ implement the insertion sort algorithm """
    # Process:
    # Compare first unsorted item
    # Insert that unsorted item in the proper spot in the sorted list
    # We will know we are at the "proper spot" when...
        # We reach the end of the list (meaning current is the largest) OR
        # We reach an equal number (put current before existing) OR
        # We reach a point where current is greater than previous value
            # but less than next value. Or there is no previous value.
    
    # i will represent the unsorted position we are currently at.
    for i in range(1, len(items)):
        current_item = items[i]
        
        # j represents the sorted item we are comparing to.
        j = i - 1
        right_item = items[j]
        
        # Fakes the swapping by moving the item to the correct position one at a time.
        while current_item < right_item and j >= 0:
            temp = items[j]
            items[j] = current_item
            items[j+1] = temp
            
            right_item = items[j-1]
            j -= 1
            
        print(items)
            
    return items
    
def main():
    
    print("~~~  List 1  ~~~")
    items_1 = [34, 13, 5, 23, 56, 17, 3]
    print(insertion_sort(items_1))
    
    print("~~~  List 2  ~~~")
    items_2 = [1, 2, 3, 4, 5]
    print(insertion_sort(items_2))
    
main()