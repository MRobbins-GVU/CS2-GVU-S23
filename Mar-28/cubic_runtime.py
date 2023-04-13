# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

def main():
    
    start = time.time()
    n = 50
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                print(x,y,z)
                count+=1
    end = time.time()
    print(end-start)
    print(count)
    
    
    
main()
