# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:06:21 2023

@author: mrobbins
"""


def selection_sort(items):
    """ Sort items using selection sort """
    for i in range(len(items)):
        # Assume the first item is the largest
        largest_idx = 0
        
        for j in range(len(items) - i):
            if items[largest_idx] < items[j]:
                largest_idx = j
            print(items)

        temp = items[largest_idx]
        
        items[largest_idx] = items[len(items)-i-1]
        
        items[len(items)-i-1] = temp
        
    return items

        
        
    
def main():
    items1 = [34, 13, 5, 23, 56, 17, 3]
    
    print("***list1: ***")
    sorted_items = selection_sort(items1)
    print(sorted_items)
    
    print("***list2: ***")
    items2 = [3,3,3,3,3]
    print(selection_sort(items2))
    
    print("***list3: ***")
    items3 = [1,2,3,4,5]
    print(selection_sort(items3))
    
    
main()