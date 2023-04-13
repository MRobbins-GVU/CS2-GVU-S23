# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:10:03 2023

@author: mrobbins
"""

def factorial_recursive(n):
    """ Use recursion to calculate a factorial """
    if n == 0:
        return 1
    elif n > 0:
        return n*factorial_recursive(n-1)
    
    
def factorial_while(n):
    """ Use a while loop to calculate a factorial """
    total = 1
    while n >= 1:
        # print(n)
        total *= n
        n -= 1
    
    return total
    
    
def main():
    print(factorial_recursive(5))
    print(factorial_while(5))
    
    
main()