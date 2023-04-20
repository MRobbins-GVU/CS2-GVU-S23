# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:17:39 2023

@author: mrobbins
"""



def bubble_sort(items):
    """ sort items list using bubble sort """
    
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j+1]:
                temp = items[j+1] 
                items[j+1] = items[j]
                items[j] = temp
            print(items)
    
    return items
    
    
def main():
    items1 = [34, 13, 5, 23, 56, 17, 3]
    
    items1_sorted = bubble_sort(items1)
    
    print(items1)
    print(items1_sorted)
    
    sorted_list = [1,2,3,4,5]
    print(bubble_sort(sorted_list))
    
main()