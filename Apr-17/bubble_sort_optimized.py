# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:47:15 2023

@author: mrobbins
"""


def bubble_sort_opt(items):
    """ sort items list using bubble sort """
    
    for i in range(len(items)):
        swapped = False
        for j in range(len(items) - 1 - i):
            if items[j] > items[j+1]:
                swapped = True
                temp = items[j+1] 
                items[j+1] = items[j]
                items[j] = temp
            print(items)

        if swapped == False:
            # We know that the rest is sorted
            print("returned early. i: ", i)
            return items
    
    return items
    
    
def main():
    items1 = [34, 13, 5, 23, 56, 17, 3]
    print("~~~~ Oooo ahhh sorting magic ~~~~")
    
    print(items1)  
    items1_sorted = bubble_sort_opt(items1)

    print(items1_sorted)
    
    sorted_list = [1,2,3,4,5]
    print(bubble_sort_opt(sorted_list))
    
    
main()