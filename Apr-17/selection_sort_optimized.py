# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:06:21 2023

@author: mrobbins
"""


def selection_sort_opt(items):
    """ Sort items using selection sort """
    for i in range(len(items)):
        # Assume the first item is the largest
        largest_idx = 0
        num_index_comps = 0
        
        for j in range(len(items) - i):
            if items[largest_idx] < items[j]:
                largest_idx = j
                num_index_comps += 1
            print(items)

        if num_index_comps == len(items)-i-1:
            # If we know all of the items are greater
            # than the ones before, the list is sorted.
            print("Returned early. i: ", i)
            return items

        temp = items[largest_idx]
        
        items[largest_idx] = items[len(items)-i-1]
        
        items[len(items)-i-1] = temp
        
    return items

        
        
    
def main():
    items1 = [34, 13, 5, 23, 56, 17, 3]
    
    print("***list1: ***")
    sorted_items = selection_sort_opt(items1)
    print(sorted_items)
    
    print("***list2: ***")
    items2 = [3,3,3,3,3]
    print(selection_sort_opt(items2))
    
    print("***list3: ***")
    items3 = [1,2,3,4,5]
    print(selection_sort_opt(items3))
    
    
main()