# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:37:32 2023

@author: mrobbins
"""

def fib(n):
    if n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    elif n > 2:
        return fib(n-1) + fib(n-2)
    

def main():
    print(fib(6))
    
main()

